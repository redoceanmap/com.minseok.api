from pydantic import BaseModel


class ModelInfoResponseSchema(BaseModel):
    model: str
    accuracy: float


class ModelTreeResponseSchema(BaseModel):
    tree: str
