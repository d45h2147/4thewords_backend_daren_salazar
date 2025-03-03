from fastapi import APIRouter
from app.routes import legend_routes, legends_routes, location_routes, category_routes

api_router = APIRouter()
api_router.include_router(legend_routes.router, prefix="/legend", tags=["legend"])
api_router.include_router(legends_routes.router, prefix="/legends", tags=["legends"])
api_router.include_router(location_routes.router, prefix="/location", tags=["location"])
api_router.include_router(category_routes.router, prefix="/categories", tags=["categories"])
