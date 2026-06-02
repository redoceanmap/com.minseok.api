import logging

from backend.apps.titanic.app.ports.output.isidor_query_repository import IsidorQueryRepository
from backend.apps.titanic.domain.entities.titanic_entity import TitanicPassenger
from backend.core.database import AsyncSessionLocal

logger = logging.getLogger(__name__)


class IsidorQueryPgRepository(IsidorQueryRepository):

    async def get_all_passengers(self) -> list[dict]:
        pass
