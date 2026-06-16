from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.app.dtos.detective_mary_operator_dto import MaryOperatorQuery, MaryOperatorResponse
from sherlock_homes.app.ports.output.detective_mary_operator_repository import MaryOperatorRepository

logger = logging.getLogger(__name__)


class MaryOperatorPgRepository(MaryOperatorRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: MaryOperatorQuery) -> MaryOperatorResponse:
        '''메리 왓슨 (Mary)의 자기 소개 레포지토리 구현 메소드'''
        logger.info(f"[MaryOperatorPgRepository] introduce_myself 진입 | request_data={query}")
        return MaryOperatorResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
