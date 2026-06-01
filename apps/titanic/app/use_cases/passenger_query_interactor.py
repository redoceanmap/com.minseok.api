import logging
from backend.apps.titanic.app.ports.input.passenger_query_use_case import PassengerQueryUseCasePort
from backend.apps.titanic.app.ports.output.passenger_query_repository import PassengerQueryRepositoryPort

logger = logging.getLogger(__name__)


class PassengerQueryInteractor(PassengerQueryUseCasePort):

    def __init__(self, passenger_repository: PassengerQueryRepositoryPort) -> None:
        self._passenger_repository = passenger_repository

    async def get_count(self) -> int:
        return await self._passenger_repository.get_count()

    async def get_survived(self) -> int:
        return await self._passenger_repository.get_survived()

    async def get_dead(self) -> int:
        return await self._passenger_repository.get_dead()
