from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile, Form, Depends
from typing import List

from app.controllers.v1.legend_controller import LegendController
from app.schemas.legend_schema import LegendBase, LegendUpdate, LegendResponseDTO, data_create_legend

router = APIRouter()


@router.post("", response_model=LegendResponseDTO, status_code=status.HTTP_201_CREATED)
async def create_legend(
    file: UploadFile = File(...),
    legend: LegendBase = Depends(data_create_legend),
    controller: LegendController = Depends()
):
    legend = await controller.create_legend(file, legend)
    return legend


@router.put("/{legend_id}", response_model=LegendResponseDTO)
async def update_legend(
    legend_id: int,
    file: UploadFile = File(...),
    legend: LegendBase = Depends(data_create_legend),
    controller: LegendController = Depends()
):
    legend = await controller.update(legend_id, legend, file)
    if not legend:
        # TODO: config logger pending
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return legend


@router.delete("/{legend_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_legend(legend_id: int, controller: LegendController = Depends()):
    success = await controller.delete(legend_id)
    if not success:
        # TODO: config logger pending
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return None
