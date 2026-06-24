from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.app.dtos.detective_watson_executor_dto import WatsonExecutorQuery, WatsonExecutorResponse
from sherlock_homes.app.ports.output.detective_watson_executor_repository import WatsonExecutorRepository

logger = logging.getLogger(__name__)


class WatsonExecutorPgRepository(WatsonExecutorRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: WatsonExecutorQuery) -> WatsonExecutorResponse:
        '''존 왓슨의 자기 소개 레포지토리 구현 메소드'''
        logger.info(f"[WatsonExecutorPgRepository] introduce_myself 진입 | request_data={query}")
        return WatsonExecutorResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
