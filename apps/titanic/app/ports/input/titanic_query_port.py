from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class TitanicQueryPort(ABC):

    @abstractmethod
    def get_model_name(self) -> str:
        pass

    @abstractmethod
    def get_tree(self) -> str:
        pass

    @abstractmethod
    def get_accuracy(self) -> float:
        pass

    @abstractmethod
    async def get_data(self, session: AsyncSession) -> list[dict]:
        pass

    @abstractmethod
    async def get_count(self, session: AsyncSession) -> int:
        pass

    @abstractmethod
    async def get_survived(self, session: AsyncSession) -> int:
        pass

    @abstractmethod
    async def get_dead(self, session: AsyncSession) -> int:
        pass
