from fastapi import HTTPException, UploadFile, status, Depends
from typing import List, Optional
from sqlmodel import Session


from app.core.database import get_session
from app.services.legend_service import LegendService
from app.schemas.legend_schema import LegendBase, LegendUpdate, LegendResponseDTO


class LegendController:
    def __init__(self, session: Session = Depends(get_session)):
        self.legend_service = LegendService(session)

    async def get_batch(self) -> List[LegendResponseDTO]:
        try:
            result = await self.legend_service.get_batch()
            return result
        except Exception as e:
            # TODO: config logger pending
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error obtener Leyendas"
            )

    async def get_by_id(self, legend_id: int) -> Optional[LegendResponseDTO]:
        try:
            result = await self.legend_service.get_by_id(legend_id)
            return result
        except Exception as e:
            # TODO: config logger pending
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al obtener Leyenda"
            )

    async def create_legend(self, file: UploadFile,  legend: LegendBase) -> LegendResponseDTO:
        try:
            result = await self.legend_service.create(file, legend)
            return result
        except Exception as e:
            # TODO: config logger pending
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al crear Leyenda"
            )

    async def update(self, legend_id: int, legend: LegendUpdate, file: UploadFile) -> Optional[LegendResponseDTO]:
        try:
            result = await self.legend_service.update(legend_id, legend, file)
            return result
        except Exception as e:
            # TODO: config logger pending
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al actualizar Leyenda"
            )

    async def delete(self, legend_id: int) -> bool:
        try:
            result = await self.legend_service.delete(legend_id)
            return result
        except Exception as e:
            # TODO: config logger pending
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al eliminar Leyenda"
            )
