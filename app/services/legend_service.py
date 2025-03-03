from fastapi import UploadFile
from sqlmodel import Session, select
from typing import List, Optional

from app.core.s3_client import s3_client
from app.schemas.legend_schema import LegendBase, LegendResponseDTO, LegendUpdate
from app.models.legend_model import Legend
from app.common.datetime import get_current_date


class LegendService:
    def __init__(self, session: Session):
        self.session = session

    async def get_batch(self) -> List[LegendResponseDTO]:
        query = select(Legend).where(Legend.deleted_at == None)
        result = self.session.exec(query)
        return result

    async def get_by_id(self, legend_id: int) -> List[LegendResponseDTO]:
        query = select(Legend).where(Legend.id == legend_id)
        result = self.session.exec(query)
        return result

    async def create(self, file: UploadFile, legend_data: LegendBase) -> LegendResponseDTO:
        new_legend = Legend(**legend_data.model_dump())
        new_legend.image_url = await self._upload_file(file)
        self.session.add(new_legend)
        self.session.commit()
        self.session.refresh(new_legend)
        return new_legend

    async def update(self, legend_id: int, legend: LegendUpdate, file: UploadFile) -> Optional[LegendResponseDTO]:
        update_legend = self.session.exec(select(Legend).where(Legend.id == legend_id)).first()
        if not update_legend:
            return None

        data_dict = legend.model_dump(exclude_unset=True)
        for key, value in data_dict.items():
            setattr(update_legend, key, value)
        update_legend.image_url = await self._upload_file(file)

        self.session.commit()
        self.session.refresh(update_legend)
        return update_legend

    async def delete(self, legend_id: int) -> bool:
        legend = self.session.exec(select(Legend).where(Legend.id == legend_id)).first()
        if not legend:
            return None
        legend.deleted_at = get_current_date()
        self.session.commit()
        return True

    async def _upload_file(self, file: UploadFile):
        ext = file.filename.split(".")[-1].lower()
        file_name = get_current_date().strftime("%Y%m%d%H%M")
        full_file_name = file_name+ext
        return await s3_client.upload_file(file, full_file_name)
