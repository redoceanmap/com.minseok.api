from pydantic import BaseModel
from typing import Optional


class TitanicPassengerRequest(BaseModel):
    passenger_id: str
    survived: str
    pclass: str
    name: str
    gender: str          # CSV 원본 컬럼명 Sex
    age: Optional[str] = None
    sib_sp: str
    parch: str
    ticket: str
    fare: str
    cabin: Optional[str] = None
    embarked: Optional[str] = None
