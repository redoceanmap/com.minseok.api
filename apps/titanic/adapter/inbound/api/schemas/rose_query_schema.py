from pydantic import BaseModel


class RoseModelInfoResponseSchema(BaseModel):
    model: str
    accuracy: float


class RoseModelTreeResponseSchema(BaseModel):
    tree: str
