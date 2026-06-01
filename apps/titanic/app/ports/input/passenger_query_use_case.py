from abc import ABC, abstractmethod


class PassengerQueryUseCasePort(ABC):

    @abstractmethod
    async def get_count(self) -> int: ...

    @abstractmethod
    async def get_survived(self) -> int: ...

    @abstractmethod
    async def get_dead(self) -> int: ...
