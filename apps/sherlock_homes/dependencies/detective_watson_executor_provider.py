from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.adapter.outbound.pg.detective_watson_executor_pg_repository import WatsonExecutorPgRepository
from sherlock_homes.app.ports.output.detective_watson_executor_repository import WatsonExecutorRepository
from core.matrix.grid_oracle_database_manager import get_db
from sherlock_homes.app.ports.input.detective_watson_executor_use_case import WatsonExecutorUseCase
from sherlock_homes.app.use_cases.detective_watson_executor_interactor import WatsonExecutorInteractor

'''
캐릭터: 존 왓슨 (John)
'''

def get_watson_executor_use_case(
        db: AsyncSession = Depends(get_db)
) -> WatsonExecutorUseCase:
    repository: WatsonExecutorRepository = WatsonExecutorPgRepository(session=db)
    return WatsonExecutorInteractor(repository=repository)
