from abc import ABC, abstractmethod


class AndrewsQueryRepository(ABC):

    @abstractmethod
    async def get_all_passengers(self) -> list[dict]:
        pass
