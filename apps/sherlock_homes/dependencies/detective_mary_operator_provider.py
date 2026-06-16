from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.adapter.outbound.pg.detective_mary_operator_pg_repository import MaryOperatorPgRepository
from sherlock_homes.app.ports.output.detective_mary_operator_repository import MaryOperatorRepository
from core.matrix.grid_oracle_database_manager import get_db
from sherlock_homes.app.ports.input.detective_mary_operator_use_case import MaryOperatorUseCase
from sherlock_homes.app.use_cases.detective_mary_operator_interactor import MaryOperatorInteractor

'''
캐릭터: 메리 왓슨 (Mary)
'''

def get_mary_operator_use_case(
        db: AsyncSession = Depends(get_db)
) -> MaryOperatorUseCase:
    repository: MaryOperatorRepository = MaryOperatorPgRepository(session=db)
    return MaryOperatorInteractor(repository=repository)
