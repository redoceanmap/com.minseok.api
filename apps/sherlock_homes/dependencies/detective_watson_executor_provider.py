from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.adapter.outbound.pg.detective_watson_executor_pg_repository import WatsonExecutorPgRepository
from sherlock_homes.app.ports.output.detective_watson_executor_repository import WatsonExecutorRepository
from core.matrix.grid_oracle_database_manager import get_db
from sherlock_homes.app.ports.input.detective_watson_executor_use_case import WatsonExecutorUseCase
from sherlock_homes.app.use_cases.detective_watson_executor_interactor import WatsonExecutorInteractor

'''
캐릭터: 존 왓슨 (John)
역할 (keyword): executor (실행/조율자)
드라마 설정 및 시스템 기능: 셜록의 파트너인 사설 탐정 조력자.
탐정의 추론 결과를 실제 현실 세계의 액션과 인간의 언어(블로그 등)로 번역하고 최종 사용자 인터페이스를 조율 및 실행합니다.
'''

def get_watson_executor_use_case(
        db: AsyncSession = Depends(get_db)
) -> WatsonExecutorUseCase:
    repository: WatsonExecutorRepository = WatsonExecutorPgRepository(session=db)
    return WatsonExecutorInteractor(repository=repository)
