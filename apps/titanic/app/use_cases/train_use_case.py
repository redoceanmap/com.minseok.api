from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from titanic.app.models.rose_model import RoseModel
from backend.apps.titanic.app.use_cases.reader_use_case import WalterRepository


class JackService:

    def __init__(self, rose: RoseModel, walter: WalterRepository):
        self.rose = rose
        self.walter = walter

    @classmethod
    async def create(cls, session: AsyncSession) -> Optional["JackService"]:
        walter = WalterRepository()
        df = await walter.get_all_as_dataframe(session)
        if df.empty:
            return None
        rose = RoseModel(df)
        return cls(rose, walter)

    def get_model(self) -> str:
        return self.rose.get_model()

    def get_accuracy(self) -> float:
        return self.rose.get_accuracy()

    def get_tree(self) -> str:
        return self.rose.get_tree()

    async def get_data(self, session: AsyncSession) -> list[dict]:
        return await self.walter.get_data(session)

    async def get_count(self, session: AsyncSession) -> int:
        return await self.walter.get_count(session)

    async def get_survived(self, session: AsyncSession) -> int:
        return await self.walter.get_survived(session)

    async def get_dead(self, session: AsyncSession) -> int:
        return await self.walter.get_dead(session)
