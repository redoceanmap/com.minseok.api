import logging
import pandas as pd
from sqlalchemy import func, select
from backend.core.database import AsyncSessionLocal
from backend.apps.titanic.domain.entities.titanic_entity import TitanicPassenger

logger = logging.getLogger(__name__)


class JackPgRepository:

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

    async def get_all_as_dataframe(self) -> pd.DataFrame:
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(TitanicPassenger))
            rows = result.scalars().all()
        return pd.DataFrame([self._to_dict(r) for r in rows])

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
            "Boat": row.boat,
            "Embarked": row.embarked,
        }
