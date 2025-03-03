from sqlmodel import Session, select
from typing import List

from app.schemas.legend_schema import CategoryDTO
from app.models.legend_model import Category


class CategoryService:
    def __init__(self, session: Session):
        self.session = session

    async def get_categories(self) -> List[CategoryDTO]:
        query = select(Category)
        result = self.session.exec(query)
        return result
