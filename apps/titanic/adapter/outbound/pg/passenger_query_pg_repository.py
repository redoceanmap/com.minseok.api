import logging
from sqlalchemy import func, select
from backend.core.database import AsyncSessionLocal
from backend.apps.titanic.domain.entities.titanic_entity import TitanicPassenger
from backend.apps.titanic.app.ports.output.passenger_query_repository import PassengerQueryRepositoryPort

logger = logging.getLogger(__name__)


class PassengerQueryPgRepository(PassengerQueryRepositoryPort):

    async def get_count(self) -> int:
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(func.count()).select_from(TitanicPassenger))
            return result.scalar() or 0

    async def get_survived(self) -> int:
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(func.count()).where(TitanicPassenger.survived == 1)
            )
            return result.scalar() or 0

    async def get_dead(self) -> int:
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(func.count()).where(TitanicPassenger.survived == 0)
            )
            return result.scalar() or 0
