from abc import ABC, abstractmethod

from backend.apps.titanic.adapter.inbound.api.schemas.james_command_schema import TitanicPassengerRequestSchema


class JamesCommandUseCase(ABC):

    @abstractmethod
    async def upload_passengers(self, passengers: list[TitanicPassengerRequestSchema]) -> dict:
        """CSV 파일 업로드"""
        pass
