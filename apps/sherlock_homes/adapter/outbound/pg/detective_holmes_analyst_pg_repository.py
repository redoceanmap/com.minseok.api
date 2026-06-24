from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.app.dtos.detective_holmes_analyst_dto import HolmesAnalystQuery, HolmesAnalystResponse
from sherlock_homes.app.ports.output.detective_holmes_analyst_repository import HolmesAnalystRepository

logger = logging.getLogger(__name__)


class HolmesAnalystPgRepository(HolmesAnalystRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: HolmesAnalystQuery) -> HolmesAnalystResponse:
        '''셜록 홈즈의 자기 소개 레포지토리 구현 메소드'''
        logger.info(f"[HolmesAnalystPgRepository] introduce_myself 진입 | request_data={query}")
        return HolmesAnalystResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
