from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.app.dtos.police_lestrade_adapter_dto import LestradeAdapterQuery, LestradeAdapterResponse
from sherlock_homes.app.ports.output.police_lestrade_adapter_repository import LestradeAdapterRepository

logger = logging.getLogger(__name__)


class LestradeAdapterPgRepository(LestradeAdapterRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: LestradeAdapterQuery) -> LestradeAdapterResponse:
        '''레스트레이드 경감 (Lestrade)의 자기 소개 레포지토리 구현 메소드'''
        logger.info(f"[LestradeAdapterPgRepository] introduce_myself 진입 | request_data={query}")
        return LestradeAdapterResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
