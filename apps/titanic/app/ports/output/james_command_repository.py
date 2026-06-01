from abc import ABC, abstractmethod

from backend.apps.titanic.adapter.inbound.api.schemas.james_command_schema import TitanicPassengerRequestSchema


class JamesCommandRepository(ABC):

    @abstractmethod
    async def save_passengers(self, passengers: list[TitanicPassengerRequestSchema]) -> None:
        pass
