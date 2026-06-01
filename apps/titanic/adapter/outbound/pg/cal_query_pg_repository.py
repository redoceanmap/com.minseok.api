import logging

from backend.apps.titanic.app.ports.output.cal_query_repository import CalQueryRepository
from backend.apps.titanic.domain.entities.titanic_entity import TitanicPassenger
from backend.core.database import AsyncSessionLocal

logger = logging.getLogger("cal.outbound.cal_query_pg_repository")


class CalQueryPgRepository(CalQueryRepository):

    async def get_all_passengers(self) -> list[dict]:
        pass
