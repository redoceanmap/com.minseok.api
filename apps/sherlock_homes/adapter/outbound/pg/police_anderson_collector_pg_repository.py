from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.app.dtos.police_anderson_collector_dto import AndersonCollectorQuery, AndersonCollectorResponse
from sherlock_homes.app.ports.output.police_anderson_collector_repository import AndersonCollectorRepository

logger = logging.getLogger(__name__)


class AndersonCollectorPgRepository(AndersonCollectorRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: AndersonCollectorQuery) -> AndersonCollectorResponse:
        '''앤더슨의 자기 소개 레포지토리 구현 메소드'''
        logger.info(f"[AndersonCollectorPgRepository] introduce_myself 진입 | request_data={query}")
        return AndersonCollectorResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
