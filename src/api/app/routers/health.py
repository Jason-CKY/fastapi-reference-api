from fastapi import APIRouter
from app.schemas.health import HealthCheckResponse

router = APIRouter()


@router.get(
    "/health", response_model=HealthCheckResponse, include_in_schema=False
)
def healthcheck():
    return HealthCheckResponse(status="Healthy")
