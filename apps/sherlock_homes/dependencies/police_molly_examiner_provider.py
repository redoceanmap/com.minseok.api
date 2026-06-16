from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.adapter.outbound.pg.police_molly_examiner_pg_repository import MollyExaminerPgRepository
from sherlock_homes.app.ports.output.police_molly_examiner_repository import MollyExaminerRepository
from core.matrix.grid_oracle_database_manager import get_db
from sherlock_homes.app.ports.input.police_molly_examiner_use_case import MollyExaminerUseCase
from sherlock_homes.app.use_cases.police_molly_examiner_interactor import MollyExaminerInteractor

'''
캐릭터: 몰리 후퍼 (Molly)
'''

def get_molly_examiner_use_case(
        db: AsyncSession = Depends(get_db)
) -> MollyExaminerUseCase:
    repository: MollyExaminerRepository = MollyExaminerPgRepository(session=db)
    return MollyExaminerInteractor(repository=repository)
