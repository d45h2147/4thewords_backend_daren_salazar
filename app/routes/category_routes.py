from fastapi import APIRouter, Depends, Depends
from typing import List

from app.controllers.v1.category_controller import CategoryController
from app.schemas.legend_schema import CategoryDTO

router = APIRouter()


@router.get("", response_model=List[CategoryDTO])
async def get_categories(controller: CategoryController = Depends()):
    categories = await controller.get_categories()
    return categories
