from fastapi import UploadFile, HTTPException
from botocore.exceptions import ClientError
import mimetypes
import boto3
import asyncio
import json

from app.core.settings import app_setting
from app.common.singleton import singleton


@singleton
class S3Client:
    def __init__(self):
        print(app_setting.s3_endpoint)
        self.client = boto3.client(
            "s3",
            endpoint_url=app_setting.s3_endpoint,
            aws_access_key_id=app_setting.s3_access_key,
            aws_secret_access_key=app_setting.s3_secret_key,
        )
        self.bucket_name = app_setting.s3_bucket_name
        self.allowed_extensions = {"jpg", "jpeg", "png", "gif"}
        self.max_file_size = 5 * 1024 * 1024
        self._ensure_bucket_exists()

    def _ensure_bucket_exists(self):
        try:
            self.client.head_bucket(Bucket=self.bucket_name)
        except ClientError:
            self.client.create_bucket(ACL="public-read", Bucket=self.bucket_name)
            public_policy = {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {"AWS": ["*"]},
                        "Action": [
                            "s3:AbortMultipartUpload",
                            "s3:DeleteObject",
                            "s3:GetObject",
                            "s3:ListMultipartUploadParts",
                            "s3:PutObject"
                        ],
                        "Resource": [f"arn:aws:s3:::{self.bucket_name}/*"]
                    }
                ],
            }

            self.client.put_bucket_policy(
                Bucket=self.bucket_name,
                Policy=json.dumps(public_policy),
            )

    def _validate_file(self, file: UploadFile):
        ext = file.filename.split(".")[-1].lower()
        if ext not in self.allowed_extensions:
            raise HTTPException(status_code=400, detail="Formato de archivo no permitido")

        file.file.seek(0, 2)
        file_size = file.file.tell()
        file.file.seek(0)

        if file_size > self.max_file_size:
            raise HTTPException(status_code=400, detail="El archivo excede el tamaño máximo permitido")

    async def upload_file(self, file: UploadFile, file_name: str):
        self._validate_file(file)
        content_type = mimetypes.guess_type(file.filename)[0] or "application/octet-stream"

        loop = asyncio.get_running_loop()
        try:
            await loop.run_in_executor(
                None,
                lambda: self.client.upload_fileobj(
                    file.file,
                    self.bucket_name,
                    file_name,
                    ExtraArgs={"ContentType": content_type,  "ACL": "public-read"},
                )
            )
        except ClientError as e:
            raise HTTPException(status_code=500, detail=f"Error subiendo archivo: {str(e)}")

        return f"{app_setting.s3_endpoint}/{self.bucket_name}/{file_name}"


s3_client = S3Client()
