from pydantic import BaseModel


class ModelInfoDto(BaseModel):
    model: str
    accuracy: float


class ModelTreeDto(BaseModel):
    tree: str
