from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.adapter.outbound.pg.police_anderson_collector_pg_repository import AndersonCollectorPgRepository
from sherlock_homes.app.ports.output.police_anderson_collector_repository import AndersonCollectorRepository
from core.matrix.grid_oracle_database_manager import get_db
from sherlock_homes.app.ports.input.police_anderson_collector_use_case import AndersonCollectorUseCase
from sherlock_homes.app.use_cases.police_anderson_collector_interactor import AndersonCollectorInteractor

'''
캐릭터: 앤더슨 (Anderson)
'''

def get_anderson_collector_use_case(
        db: AsyncSession = Depends(get_db)
) -> AndersonCollectorUseCase:
    repository: AndersonCollectorRepository = AndersonCollectorPgRepository(session=db)
    return AndersonCollectorInteractor(repository=repository)
