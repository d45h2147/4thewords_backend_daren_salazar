from fastapi import HTTPException, status, Depends
from typing import List
from sqlmodel import Session


from app.core.database import get_session
from app.services.location_service import LocationService
from app.schemas.legend_schema import CantonDTO, ProvinceDTO, DistrictDTO


class LocationController:
    def __init__(self, session: Session = Depends(get_session)):
        self.location_service = LocationService(session)

    async def get_cantons(self) -> List[CantonDTO]:
        try:
            result = await self.location_service.get_cantons()
            return result
        except Exception as e:
            # TODO: config logger pending
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error obtener cantons"
            )

    async def get_provinces(self) -> List[ProvinceDTO]:
        try:
            result = await self.location_service.get_provinces()
            return result
        except Exception as e:
            # TODO: config logger pending
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error obtener provinces"
            )

    async def get_districts(self) -> List[DistrictDTO]:
        try:
            result = await self.location_service.get_districts()
            return result
        except Exception as e:
            # TODO: config logger pending
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error obtener districts"
            )
