from typing import Optional

from backend.apps.titanic.app.use_cases.rose_query_interactor import RoseModel
from backend.apps.titanic.adapter.outbound.pg.jack_pg_repository import JackPgRepository


class JackService:

    def __init__(self, rose: RoseModel):
        self.rose = rose

    @classmethod
    async def create(cls) -> Optional["JackService"]:
        jack_repo = JackPgRepository()
        df = await jack_repo.get_all_as_dataframe()
        if df.empty:
            return None
        rose = RoseModel(df)
        return cls(rose)

    def get_model(self) -> str:
        return self.rose.get_model()

    def get_accuracy(self) -> float:
        return self.rose.get_accuracy()

    def get_tree(self) -> str:
        return self.rose.get_tree()

