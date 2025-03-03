from sqlmodel import Session, select
from typing import List

from app.schemas.legend_schema import CantonDTO, ProvinceDTO, DistrictDTO
from app.models.legend_model import Canton, Province, District


class LocationService:
    def __init__(self, session: Session):
        self.session = session

    async def get_cantons(self) -> List[CantonDTO]:
        query = select(Canton)
        result = self.session.exec(query)
        return result

    async def get_provinces(self) -> List[ProvinceDTO]:
        query = select(Province)
        result = self.session.exec(query)
        return result

    async def get_districts(self) -> List[DistrictDTO]:
        query = select(District)
        result = self.session.exec(query)
        return result
