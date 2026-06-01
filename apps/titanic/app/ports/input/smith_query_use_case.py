from abc import ABC, abstractmethod


class SmithQueryUseCase(ABC):

    @abstractmethod
    async def get_passengers(self) -> list[dict]:
        pass
