import logging

from backend.apps.titanic.app.ports.input.andrews_query_use_case import AndrewsQueryUseCase
from backend.apps.titanic.app.ports.output.andrews_query_repository import AndrewsQueryRepository

logger = logging.getLogger(__name__)


class AndrewsQueryInteractor(AndrewsQueryUseCase):

    def __init__(self, repository: AndrewsQueryRepository) -> None:
        self.repository = repository

    async def get_passengers(self) -> list[dict]:
        return await self.repository.get_all_passengers()
