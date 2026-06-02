import logging

from backend.apps.titanic.app.ports.input.hartlery_query_use_case import HartleryQueryUseCase
from backend.apps.titanic.app.ports.output.hartlery_query_repository import HartleryQueryRepository

logger = logging.getLogger(__name__)


class HartleryQueryInteractor(HartleryQueryUseCase):

    def __init__(self, repository: HartleryQueryRepository) -> None:
        self.repository = repository

    async def get_passengers(self) -> list[dict]:
        return await self.repository.get_all_passengers()
