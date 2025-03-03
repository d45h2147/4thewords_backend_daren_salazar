from fastapi import APIRouter, Depends, Depends
from typing import List

from app.controllers.v1.location_controller import LocationController
from app.schemas.legend_schema import CantonDTO, ProvinceDTO, DistrictDTO

router = APIRouter()


@router.get("/cantons", response_model=List[CantonDTO])
async def get_cantons(controller: LocationController = Depends()):
    cantons = await controller.get_cantons()
    return cantons


@router.get("/provinces", response_model=List[ProvinceDTO])
async def get_provinces(controller: LocationController = Depends()):
    provinces = await controller.get_provinces()
    return provinces


@router.get("/districts", response_model=List[DistrictDTO])
async def get_districts(controller: LocationController = Depends()):
    districts = await controller.get_districts()
    return districts
