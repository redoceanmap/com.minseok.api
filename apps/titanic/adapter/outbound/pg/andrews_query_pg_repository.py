import logging

from backend.apps.titanic.app.ports.output.andrews_query_repository import AndrewsQueryRepository
from backend.apps.titanic.domain.entities.titanic_entity import TitanicPassenger
from backend.core.database import AsyncSessionLocal

logger = logging.getLogger(__name__)


class AndrewsQueryPgRepository(AndrewsQueryRepository):

    async def get_all_passengers(self) -> list[dict]:
        pass
