from abc import ABC, abstractmethod


class HartleryQueryUseCase(ABC):

    @abstractmethod
    async def get_passengers(self) -> list[dict]:
        pass
