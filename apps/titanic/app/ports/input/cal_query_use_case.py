from abc import ABC, abstractmethod


class CalQueryUseCase(ABC):

    @abstractmethod
    async def get_passengers(self) -> list[dict]:
        pass
