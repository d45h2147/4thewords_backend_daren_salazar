from fastapi import HTTPException, status, Depends
from typing import List
from sqlmodel import Session


from app.core.database import get_session
from app.services.category_service import CategoryService
from app.schemas.legend_schema import CategoryDTO


class CategoryController:
    def __init__(self, session: Session = Depends(get_session)):
        self.category_service = CategoryService(session)

    async def get_categories(self) -> List[CategoryDTO]:
        try:
            result = await self.category_service.get_categories()
            return result
        except Exception as e:
            # TODO: config logger pending
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error obtener las categorias"
            )
