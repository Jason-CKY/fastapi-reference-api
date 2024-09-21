from loguru import logger
from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
from app.core.settings import settings
from app.routers.health import router as health_router
from app.routers.query import router as query_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.debug("DEBUG starting")
    logger.info("INFO starting")
    yield


app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    docs_url=None,
    redoc_url=None,
    lifespan=lifespan,
)


@app.get("/", include_in_schema=False)
def custom_docs():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title,
        swagger_favicon_url='/static/icon/favicon.ico'
    )


app.include_router(health_router)
app.include_router(query_router, tags=["query"], prefix="/api/v1")

app.mount(
    '/static',
    StaticFiles(directory=Path(__file__).parent / 'static'),
    name='static'
)
