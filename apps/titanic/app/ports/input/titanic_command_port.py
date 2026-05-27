from abc import ABC, abstractmethod
from titanic.adapter.inbound.schemas.titanic_request import TitanicPassengerRequest


class TitanicCommandPort(ABC):

    @abstractmethod
    async def predict(self, req: TitanicPassengerRequest) -> dict:
        pass
