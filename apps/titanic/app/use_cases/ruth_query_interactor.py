import logging

from backend.apps.titanic.app.ports.input.ruth_query_use_case import RuthQueryUseCase
from backend.apps.titanic.app.ports.output.ruth_query_repository import RuthQueryRepository

logger = logging.getLogger("ruth.app.ruth_query")


class RuthQueryInteractor(RuthQueryUseCase):

    def __init__(self, repository: RuthQueryRepository) -> None:
        self.repository = repository

    async def get_passengers(self) -> list[dict]:
        return await self.repository.get_all_passengers()
