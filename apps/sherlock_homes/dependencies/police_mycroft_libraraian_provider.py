from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.adapter.outbound.pg.police_mycroft_libraraian_pg_repository import MycroftLibraraianPgRepository
from sherlock_homes.app.ports.output.police_mycroft_libraraian_repository import MycroftLibraraianRepository
from core.matrix.grid_oracle_database_manager import get_db
from sherlock_homes.app.ports.input.police_mycroft_libraraian_use_case import MycroftLibraraianUseCase
from sherlock_homes.app.use_cases.police_mycroft_libraraian_interactor import MycroftLibraraianInteractor

'''
캐릭터: 마이크로프트 홈즈 (Mycroft)
'''

def get_mycroft_libraraian_use_case(
        db: AsyncSession = Depends(get_db)
) -> MycroftLibraraianUseCase:
    repository: MycroftLibraraianRepository = MycroftLibraraianPgRepository(session=db)
    return MycroftLibraraianInteractor(repository=repository)
