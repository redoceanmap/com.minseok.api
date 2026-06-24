from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.app.dtos.criminal_irene_ilustrator_dto import IreneIlustratorQuery, IreneIlustratorResponse
from sherlock_homes.app.ports.output.criminal_irene_ilustrator_repository import IreneIlustratorRepository

logger = logging.getLogger(__name__)


class IreneIlustratorPgRepository(IreneIlustratorRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: IreneIlustratorQuery) -> IreneIlustratorResponse:
        '''아이린 애들러의 자기 소개 레포지토리 구현 메소드'''
        logger.info(f"[IreneIlustratorPgRepository] introduce_myself 진입 | request_data={query}")
        return IreneIlustratorResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
