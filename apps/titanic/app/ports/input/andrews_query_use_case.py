from abc import ABC, abstractmethod


class AndrewsQueryUseCase(ABC):

    @abstractmethod
    async def get_passengers(self) -> list[dict]:
        pass
