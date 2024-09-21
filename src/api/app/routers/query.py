from fastapi.routing import APIRouter
from app.schemas.query import QueryResponse
from typing import List

router = APIRouter()


@router.get("/query", response_model=List[QueryResponse])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
