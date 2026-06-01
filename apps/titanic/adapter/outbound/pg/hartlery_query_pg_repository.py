import logging

from backend.apps.titanic.app.ports.output.hartlery_query_repository import HartleryQueryRepository
from backend.apps.titanic.domain.entities.titanic_entity import TitanicPassenger
from backend.core.database import AsyncSessionLocal

logger = logging.getLogger("hartlery.outbound.hartlery_query_pg_repository")


class HartleryQueryPgRepository(HartleryQueryRepository):

    async def get_all_passengers(self) -> list[dict]:
        pass
