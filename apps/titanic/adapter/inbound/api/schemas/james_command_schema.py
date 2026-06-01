from pydantic import BaseModel


class TitanicPassengerRequestSchema(BaseModel):
    passenger_id: str
    survived: str
    pclass: str
    name: str
    gender: str
    age: str | None = None
    sib_sp: str
    parch: str
    ticket: str
    fare: str
    cabin: str | None = None
    embarked: str | None = None
