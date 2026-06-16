from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.adapter.outbound.pg.criminal_eurus_prophet_pg_repository import EurusProphetPgRepository
from sherlock_homes.app.ports.output.criminal_eurus_prophet_repository import EurusProphetRepository
from core.matrix.grid_oracle_database_manager import get_db
from sherlock_homes.app.ports.input.criminal_eurus_prophet_use_case import EurusProphetUseCase
from sherlock_homes.app.use_cases.criminal_eurus_prophet_interactor import EurusProphetInteractor

'''
캐릭터: 유라루스 홈즈 (Eurus)
'''

def get_eurus_prophet_use_case(
        db: AsyncSession = Depends(get_db)
) -> EurusProphetUseCase:
    repository: EurusProphetRepository = EurusProphetPgRepository(session=db)
    return EurusProphetInteractor(repository=repository)
