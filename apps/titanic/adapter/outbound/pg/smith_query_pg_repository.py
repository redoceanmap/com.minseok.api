import logging

from backend.apps.titanic.app.ports.output.smith_query_repository import SmithQueryRepository
from backend.apps.titanic.domain.entities.titanic_entity import TitanicPassenger
from backend.core.database import AsyncSessionLocal

logger = logging.getLogger("smith.outbound.smith_query_pg_repository")


class SmithQueryPgRepository(SmithQueryRepository):

    async def get_all_passengers(self) -> list[dict]:
        pass
