from pydantic.dataclasses import dataclass


@dataclass
class PersonCommand:
    passenger_id: str
    name: str
    gender: str
    sib_sp: str
    parch: str
    survived: str
    age: str | None = None


@dataclass
class BookingCommand:
    pclass: str
    ticket: str
    fare: str
    cabin: str | None = None
    embarked: str | None = None


@dataclass
class PassengerCommand:
    person: PersonCommand
    booking: BookingCommand
