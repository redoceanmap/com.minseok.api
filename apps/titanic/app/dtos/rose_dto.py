from pydantic import BaseModel


class RoseModelInfoDto(BaseModel):
    model: str
    accuracy: float


class RoseModelTreeDto(BaseModel):
    tree: str
