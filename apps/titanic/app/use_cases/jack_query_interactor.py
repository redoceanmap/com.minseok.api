import logging

from backend.apps.titanic.app.ports.input.jack_query_use_case import JackQueryUseCase
from backend.apps.titanic.app.ports.output.jack_query_repository import JackQueryRepository

logger = logging.getLogger("jack.app.jack_query")


class JackQueryInteractor(JackQueryUseCase):

    def __init__(self, repository: JackQueryRepository) -> None:
        self.repository = repository

    async def get_passengers(self) -> list[dict]:
        return await self.repository.get_all_passengers()
