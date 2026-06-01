from pydantic import BaseModel


class PassengerStatsDto(BaseModel):
    count: int
    survived: int
    dead: int
