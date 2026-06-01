from abc import ABC, abstractmethod


class CalQueryRepository(ABC):

    @abstractmethod
    async def get_all_passengers(self) -> list[dict]:
        pass
