from abc import ABC, abstractmethod


class IsidorQueryUseCase(ABC):

    @abstractmethod
    async def get_passengers(self) -> list[dict]:
        pass
