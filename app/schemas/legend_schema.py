from fastapi import Form
from datetime import datetime, date, timezone
from pydantic import BaseModel, computed_field
from typing import Optional

from dateutil.relativedelta import relativedelta
from app.common.datetime import get_current_date


class ProvinceDTO(BaseModel):
    id: int
    name: str


class CantonDTO(BaseModel):
    id: int
    name: str
    province_id: int


class DistrictDTO(BaseModel):
    id: int
    name: str
    canton_id: int


class CategoryDTO(BaseModel):
    id: int
    name: str


class LegendBase(BaseModel):
    name: str
    category_id: int
    province_id: int
    canton_id: int
    district_id: int
    description: str
    legend_date: date
    source: Optional[str] = None


async def data_create_legend(
    name: str = Form(...),
    category_id: int = Form(...),
    province_id: int = Form(...),
    canton_id: int = Form(...),
    district_id: int = Form(...),
    description: str = Form(...),
    legend_date: str = Form(...),
    source: Optional[str] = Form(None)
) -> LegendBase:
    return LegendBase(
        name=name,
        category_id=category_id,
        province_id=province_id,
        canton_id=canton_id,
        district_id=district_id,
        description=description,
        legend_date=legend_date,
        source=source,
    )


class LegendUpdate(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None
    province_id: Optional[int] = None
    canton_id: Optional[int] = None
    district_id: Optional[int] = None
    description: Optional[str] = None
    legend_date: Optional[date] = None
    source: Optional[str] = None


async def data_update_legend(
    name: str = Form(None),
    category_id: int = Form(None),
    province_id: int = Form(None),
    canton_id: int = Form(None),
    district_id: int = Form(None),
    description: str = Form(None),
    legend_date: str = Form(None),
    source: Optional[str] = Form(None)
) -> LegendBase:
    return LegendBase(
        name=name,
        category_id=category_id,
        province_id=province_id,
        canton_id=canton_id,
        district_id=district_id,
        description=description,
        legend_date=legend_date,
        source=source,
    )


class LegendResponseDTO(BaseModel):
    id: int
    name: str
    description: str
    legend_date: date
    category: CategoryDTO
    province: ProvinceDTO
    canton: CantonDTO
    district: DistrictDTO
    image_url: Optional[str] = None
    source: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

    @computed_field
    @property
    def relative_created_at(self) -> str:
        """Devuelve la fecha de creación en formato relativo (hace 1 hora, hace 2 meses, hace 1 año, etc.)."""
        now = get_current_date()
        created_at_aware = self.created_at.replace(tzinfo=timezone.utc) if self.created_at.tzinfo is None else self.created_at
        delta = relativedelta(now, created_at_aware)

        if delta.years > 0:
            return f"hace {delta.years} año{'s' if delta.years > 1 else ''}"
        elif delta.months > 0:
            return f"hace {delta.months} mes{'es' if delta.months > 1 else ''}"
        elif delta.days > 0:
            return f"hace {delta.days} día{'s' if delta.days > 1 else ''}"
        elif delta.hours > 0:
            return f"hace {delta.hours} hora{'s' if delta.hours > 1 else ''}"
        elif delta.minutes > 0:
            return f"hace {delta.minutes} minuto{'s' if delta.minutes > 1 else ''}"
        else:
            return "hace unos segundos"
