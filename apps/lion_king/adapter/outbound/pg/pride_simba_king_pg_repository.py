from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from lion_king.app.dtos.pride_simba_king_dto import SimbaKingQuery, SimbaKingResponse
from lion_king.app.ports.output.pride_simba_king_repository import SimbaKingRepository

logger = logging.getLogger(__name__)


class SimbaKingPgRepository(SimbaKingRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: SimbaKingQuery) -> SimbaKingResponse:
        logger.info(f"[SimbaKingPgRepository] introduce_myself 진입 | request_data={query}")
        return SimbaKingResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
