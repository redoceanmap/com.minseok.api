from pydantic import BaseModel


class PassengerStatsResponseSchema(BaseModel):
    count: int
    survived: int
    dead: int
