from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.app.dtos.criminal_eurus_prophet_dto import EurusProphetQuery, EurusProphetResponse
from sherlock_homes.app.ports.output.criminal_eurus_prophet_repository import EurusProphetRepository

logger = logging.getLogger(__name__)


class EurusProphetPgRepository(EurusProphetRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: EurusProphetQuery) -> EurusProphetResponse:
        '''유라루스 홈즈 (Eurus)의 자기 소개 레포지토리 구현 메소드'''
        logger.info(f"[EurusProphetPgRepository] introduce_myself 진입 | request_data={query}")
        return EurusProphetResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
