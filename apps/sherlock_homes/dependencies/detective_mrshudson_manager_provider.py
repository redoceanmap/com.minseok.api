from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.adapter.outbound.pg.detective_mrshudson_manager_pg_repository import MrshudsonManagerPgRepository
from sherlock_homes.app.ports.output.detective_mrshudson_manager_repository import MrshudsonManagerRepository
from core.matrix.grid_oracle_database_manager import get_db
from sherlock_homes.app.ports.input.detective_mrshudson_manager_use_case import MrshudsonManagerUseCase
from sherlock_homes.app.use_cases.detective_mrshudson_manager_interactor import MrshudsonManagerInteractor

'''
캐릭터: 허드슨 부인 (Mrs. Hudson)
'''

def get_mrshudson_manager_use_case(
        db: AsyncSession = Depends(get_db)
) -> MrshudsonManagerUseCase:
    repository: MrshudsonManagerRepository = MrshudsonManagerPgRepository(session=db)
    return MrshudsonManagerInteractor(repository=repository)
