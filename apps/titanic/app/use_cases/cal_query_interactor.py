import logging

from backend.apps.titanic.app.ports.input.cal_query_use_case import CalQueryUseCase
from backend.apps.titanic.app.ports.output.cal_query_repository import CalQueryRepository

logger = logging.getLogger(__name__)


class CalQueryInteractor(CalQueryUseCase):

    def __init__(self, repository: CalQueryRepository) -> None:
        self.repository = repository

    async def get_passengers(self) -> list[dict]:
        return await self.repository.get_all_passengers()
