from fastapi import APIRouter, Depends, Depends
from typing import List

from app.controllers.v1.legend_controller import LegendController
from app.schemas.legend_schema import LegendResponseDTO

router = APIRouter()


@router.get("", response_model=List[LegendResponseDTO])
async def get_legends(controller: LegendController = Depends()):
    legend = await controller.get_batch()
    return legend
