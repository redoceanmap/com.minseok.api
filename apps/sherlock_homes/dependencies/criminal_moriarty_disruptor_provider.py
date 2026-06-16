from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.adapter.outbound.pg.criminal_moriarty_disruptor_pg_repository import MoriartyDisruptorPgRepository
from sherlock_homes.app.ports.output.criminal_moriarty_disruptor_repository import MoriartyDisruptorRepository
from core.matrix.grid_oracle_database_manager import get_db
from sherlock_homes.app.ports.input.criminal_moriarty_disruptor_use_case import MoriartyDisruptorUseCase
from sherlock_homes.app.use_cases.criminal_moriarty_disruptor_interactor import MoriartyDisruptorInteractor

'''
캐릭터: 모리어티 (Moriarty)
'''

def get_moriarty_disruptor_use_case(
        db: AsyncSession = Depends(get_db)
) -> MoriartyDisruptorUseCase:
    repository: MoriartyDisruptorRepository = MoriartyDisruptorPgRepository(session=db)
    return MoriartyDisruptorInteractor(repository=repository)
