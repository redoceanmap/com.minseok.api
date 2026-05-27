import pandas as pd
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from titanic.app.models.passenger_model import TitanicPassenger


class WalterRepository:

    async def get_data(self, session: AsyncSession) -> list[dict]:
        result = await session.execute(select(TitanicPassenger).limit(1))
        row = result.scalars().first()
        return [self._to_dict(row)] if row else []

    async def get_count(self, session: AsyncSession) -> int:
        result = await session.execute(select(func.count()).select_from(TitanicPassenger))
        return result.scalar() or 0

    async def get_survived(self, session: AsyncSession) -> int:
        result = await session.execute(
            select(func.count()).where(TitanicPassenger.survived == 1)
        )
        return result.scalar() or 0

    async def get_dead(self, session: AsyncSession) -> int:
        result = await session.execute(
            select(func.count()).where(TitanicPassenger.survived == 0)
        )
        return result.scalar() or 0

    async def get_all_as_dataframe(self, session: AsyncSession) -> pd.DataFrame:
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
