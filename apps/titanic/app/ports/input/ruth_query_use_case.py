from abc import ABC, abstractmethod


class RuthQueryUseCase(ABC):

    @abstractmethod
    async def get_passengers(self) -> list[dict]:
        pass
