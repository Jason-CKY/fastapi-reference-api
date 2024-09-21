from pydantic import BaseModel


class QueryResponse(BaseModel):
    username: str
