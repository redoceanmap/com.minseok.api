from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.adapter.outbound.pg.criminal_magnussen_archivist_pg_repository import MagnussenArchivistPgRepository
from sherlock_homes.app.ports.output.criminal_magnussen_archivist_repository import MagnussenArchivistRepository
from core.matrix.grid_oracle_database_manager import get_db
from sherlock_homes.app.ports.input.criminal_magnussen_archivist_use_case import MagnussenArchivistUseCase
from sherlock_homes.app.use_cases.criminal_magnussen_archivist_interactor import MagnussenArchivistInteractor

'''
캐릭터: 마그누센 (Magnussen)
'''

def get_magnussen_archivist_use_case(
        db: AsyncSession = Depends(get_db)
) -> MagnussenArchivistUseCase:
    repository: MagnussenArchivistRepository = MagnussenArchivistPgRepository(session=db)
    return MagnussenArchivistInteractor(repository=repository)
