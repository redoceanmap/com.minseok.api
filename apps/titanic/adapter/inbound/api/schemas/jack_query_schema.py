from pydantic import BaseModel


class JackPassengerResponseSchema(BaseModel):
    PassengerId: int
    Survived: int
    Pclass: int
    Name: str
    Sex: str
    Age: float | None
    SibSp: int
    Parch: int
    Ticket: str
    Fare: float
    Cabin: str | None
    Embarked: str | None
