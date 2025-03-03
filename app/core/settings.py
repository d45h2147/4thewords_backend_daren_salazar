from pydantic_settings import BaseSettings

from app.common.singleton import singleton


@singleton
class Setting(BaseSettings):
    app_name: str = "Legends Api"
    app_desc: str = ""
    version: str = "0.1.0"
    api_version: str = "/api/v1"

    db_host: str
    db_name: str
    db_user: str
    db_password: str
    s3_bucket_name: str
    s3_endpoint: str
    s3_access_key: str
    s3_secret_key: str
    
    backend_cors_origins: str

    @property
    def db_uri(self) -> str:
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}?charset=utf8mb4"

app_setting = Setting()