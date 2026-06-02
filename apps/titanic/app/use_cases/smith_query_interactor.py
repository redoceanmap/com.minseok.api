import logging

from backend.apps.titanic.app.ports.input.smith_query_use_case import SmithQueryUseCase
from backend.apps.titanic.app.ports.output.smith_query_repository import SmithQueryRepository

logger = logging.getLogger(__name__)


class SmithQueryInteractor(SmithQueryUseCase):

    def __init__(self, repository: SmithQueryRepository) -> None:
        self.repository = repository

    async def get_passengers(self) -> list[dict]:
        return await self.repository.get_all_passengers()
