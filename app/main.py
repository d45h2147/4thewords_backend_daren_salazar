from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes.api import api_router
from app.core.settings import app_setting

app = FastAPI(
    title=app_setting.app_name,
    version=app_setting.version,
    openapi_url=f"{app_setting.api_version}/openapi.json",
    description=app_setting.app_desc,
    default_response_model_exclude_unset=True,
)

origins = [origin.strip() for origin in app_setting.backend_cors_origins.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(api_router, prefix=app_setting.api_version)
