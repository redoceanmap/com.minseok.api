from abc import ABC, abstractmethod

from backend.apps.titanic.app.dtos.james_dto import PersonCommand, BookingCommand


class JamesCommandRepository(ABC):

    @abstractmethod
    async def save_passengers(self, 
                            persons: list[PersonCommand], 
                            bookings: list[BookingCommand]) -> None:
        pass
        