from datetime import datetime, date
from sqlmodel import Relationship, Field, SQLModel
from typing import Optional, List

from app.common.datetime import get_current_date


class Province(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(max_length=255, index=True)
    created_at: Optional[datetime] = Field(default_factory=get_current_date)

    cantons: List['Canton'] = Relationship(back_populates='province')
    legends: List['Legend'] = Relationship(back_populates='province')

class Canton(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(max_length=255, index=True)
    province_id: int = Field(foreign_key="province.id")
    created_at: Optional[datetime] = Field(default_factory=get_current_date)

    province: Province = Relationship(back_populates="cantons")
    districts: List["District"] = Relationship(back_populates="canton")
    legends: List["Legend"] = Relationship(back_populates="canton")

class District(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(max_length=255, index=True)
    canton_id: int = Field(foreign_key="canton.id")
    created_at: Optional[datetime] = Field(default_factory=get_current_date)

    canton: List["Canton"] = Relationship(back_populates="districts")
    legends: List["Legend"] = Relationship(back_populates="district")

class Category(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(max_length=255, index=True)
    created_at: Optional[datetime] = Field(default_factory=get_current_date)
    updated_at: Optional[datetime] = Field(default_factory=get_current_date)

    legends: List["Legend"] = Relationship(back_populates="category")


class Legend(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(max_length=255, index=True)
    category_id: int = Field(foreign_key="category.id", index=True)
    description: str
    legend_date: date
    province_id: int = Field(foreign_key="province.id", index=True)
    canton_id: int = Field(foreign_key="canton.id", index=True)
    district_id: int = Field(foreign_key="district.id", index=True)
    image_url: Optional[str] = Field(default=None, max_length=500)
    source: Optional[str] = Field(default=None, max_length=255)
    created_at: Optional[datetime] = Field(default_factory=get_current_date)
    updated_at: Optional[datetime] = Field(default_factory=get_current_date)
    deleted_at: Optional[datetime] = None

    category: Optional[Category] = Relationship(back_populates="legends")
    province: Optional[Province] = Relationship(back_populates="legends")
    canton: Optional[Canton] = Relationship(back_populates="legends")
    district: Optional[District] = Relationship(back_populates="legends")
