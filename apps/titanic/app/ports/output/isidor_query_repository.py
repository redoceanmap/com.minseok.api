from abc import ABC, abstractmethod


class IsidorQueryRepository(ABC):

    @abstractmethod
    async def get_all_passengers(self) -> list[dict]:
        pass
