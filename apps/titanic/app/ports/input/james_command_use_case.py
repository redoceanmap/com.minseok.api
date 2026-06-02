from abc import ABC, abstractmethod

from backend.apps.titanic.app.dtos.james_dto import PersonCommand, BookingCommand


class JamesCommandUseCase(ABC):

    @abstractmethod
    async def upload_passengers(self, persons: list[PersonCommand], bookings: list[BookingCommand]) -> dict:
        pass
