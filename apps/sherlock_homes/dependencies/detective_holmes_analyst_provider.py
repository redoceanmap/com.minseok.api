from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.adapter.outbound.pg.detective_holmes_analyst_pg_repository import HolmesAnalystPgRepository
from sherlock_homes.app.ports.output.detective_holmes_analyst_repository import HolmesAnalystRepository
from core.matrix.grid_oracle_database_manager import get_db
from sherlock_homes.app.ports.input.detective_holmes_analyst_use_case import HolmesAnalystUseCase
from sherlock_homes.app.use_cases.detective_holmes_analyst_interactor import HolmesAnalystInteractor

'''
캐릭터: 셜록 홈즈 (Sherlock)
'''

def get_holmes_analyst_use_case(
        db: AsyncSession = Depends(get_db)
) -> HolmesAnalystUseCase:
    repository: HolmesAnalystRepository = HolmesAnalystPgRepository(session=db)
    return HolmesAnalystInteractor(repository=repository)
