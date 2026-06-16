from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from lion_king.app.dtos.pride_nala_queen_dto import NalaQueenQuery, NalaQueenResponse
from lion_king.app.ports.output.pride_nala_queen_repository import NalaQueenRepository

logger = logging.getLogger(__name__)


class NalaQueenPgRepository(NalaQueenRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: NalaQueenQuery) -> NalaQueenResponse:
        logger.info(f"[NalaQueenPgRepository] introduce_myself 진입 | request_data={query}")
        return NalaQueenResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
