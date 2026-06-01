import logging

from backend.apps.titanic.app.ports.input.isidor_query_use_case import IsidorQueryUseCase
from backend.apps.titanic.app.ports.output.isidor_query_repository import IsidorQueryRepository

logger = logging.getLogger("isidor.app.isidor_query")


class IsidorQueryInteractor(IsidorQueryUseCase):

    def __init__(self, repository: IsidorQueryRepository) -> None:
        self.repository = repository

    async def get_passengers(self) -> list[dict]:
        return await self.repository.get_all_passengers()
