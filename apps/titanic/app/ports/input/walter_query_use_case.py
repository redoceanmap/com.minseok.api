from abc import ABC, abstractmethod


class WalterQueryUseCase(ABC):

    @abstractmethod
    async def get_passengers(self) -> list[dict]:
        pass
