import logging

from sqlalchemy import select

from backend.apps.titanic.app.ports.output.walter_query_repository import WalterQueryRepository
from backend.apps.titanic.domain.entities.titanic_entity import TitanicPassenger
from backend.core.database import AsyncSessionLocal

logger = logging.getLogger("walter.outbound.walter_query_pg_repository")


class WalterQueryPgRepository(WalterQueryRepository):

    async def get_all_passengers(self) -> list[dict]:
        logger.info("DB 조회 시작")
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(TitanicPassenger).order_by(TitanicPassenger.passenger_id)
            )
            rows = result.scalars().all()
        logger.info("DB 조회 완료 (%d건)", len(rows))
        return [self._to_dict(r) for r in rows]

    def _to_dict(self, row: TitanicPassenger) -> dict:
        return {
            "PassengerId": row.passenger_id,
            "Survived": row.survived,
            "Pclass": row.pclass,
            "Name": row.name,
            "Sex": row.sex,
            "Age": row.age,
            "SibSp": row.sib_sp,
            "Parch": row.parch,
            "Ticket": row.ticket,
            "Fare": row.fare,
            "Cabin": row.cabin,
            "Embarked": row.embarked,
        }
