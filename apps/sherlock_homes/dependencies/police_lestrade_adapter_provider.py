from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.adapter.outbound.pg.police_lestrade_adapter_pg_repository import LestradeAdapterPgRepository
from sherlock_homes.app.ports.output.police_lestrade_adapter_repository import LestradeAdapterRepository
from core.matrix.grid_oracle_database_manager import get_db
from sherlock_homes.app.ports.input.police_lestrade_adapter_use_case import LestradeAdapterUseCase
from sherlock_homes.app.use_cases.police_lestrade_adapter_interactor import LestradeAdapterInteractor

'''
캐릭터: 레스트레이드 경감 (Lestrade)
'''

def get_lestrade_adapter_use_case(
        db: AsyncSession = Depends(get_db)
) -> LestradeAdapterUseCase:
    repository: LestradeAdapterRepository = LestradeAdapterPgRepository(session=db)
    return LestradeAdapterInteractor(repository=repository)
