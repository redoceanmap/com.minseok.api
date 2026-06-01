import logging

from backend.apps.titanic.app.ports.output.ruth_query_repository import RuthQueryRepository
from backend.apps.titanic.domain.entities.titanic_entity import TitanicPassenger
from backend.core.database import AsyncSessionLocal

logger = logging.getLogger("ruth.outbound.ruth_query_pg_repository")


class RuthQueryPgRepository(RuthQueryRepository):

    async def get_all_passengers(self) -> list[dict]:
        pass
