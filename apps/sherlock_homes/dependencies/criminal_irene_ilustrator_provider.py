from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.adapter.outbound.pg.criminal_irene_ilustrator_pg_repository import IreneIlustratorPgRepository
from sherlock_homes.app.ports.output.criminal_irene_ilustrator_repository import IreneIlustratorRepository
from core.matrix.grid_oracle_database_manager import get_db
from sherlock_homes.app.ports.input.criminal_irene_ilustrator_use_case import IreneIlustratorUseCase
from sherlock_homes.app.use_cases.criminal_irene_ilustrator_interactor import IreneIlustratorInteractor

'''
캐릭터: 아이린 애들러 (Irene)
'''

def get_irene_ilustrator_use_case(
        db: AsyncSession = Depends(get_db)
) -> IreneIlustratorUseCase:
    repository: IreneIlustratorRepository = IreneIlustratorPgRepository(session=db)
    return IreneIlustratorInteractor(repository=repository)
