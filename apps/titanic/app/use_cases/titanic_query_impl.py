from sqlalchemy.ext.asyncio import AsyncSession

from titanic.app.ports.input.titanic_query_port import TitanicQueryPort
from backend.apps.titanic.app.use_cases.train_use_case import JackService


class TitanicQueryImpl(TitanicQueryPort):

    def __init__(self, jack: JackService):
        self.jack = jack

    def get_model_name(self) -> str:
        return self.jack.get_model()

    def get_tree(self) -> str:
        return self.jack.get_tree()

    def get_accuracy(self) -> float:
        return self.jack.get_accuracy()

    async def get_data(self, session: AsyncSession) -> list[dict]:
        return await self.jack.get_data(session)

    async def get_count(self, session: AsyncSession) -> int:
        return await self.jack.get_count(session)

    async def get_survived(self, session: AsyncSession) -> int:
        return await self.jack.get_survived(session)

    async def get_dead(self, session: AsyncSession) -> int:
        return await self.jack.get_dead(session)
