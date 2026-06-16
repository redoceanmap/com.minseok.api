from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from lion_king.app.dtos.savanna_pumba_warthog_dto import PumbaWarthogQuery, PumbaWarthogResponse
from lion_king.app.ports.output.savanna_pumba_warthog_repository import PumbaWarthogRepository

logger = logging.getLogger(__name__)


class PumbaWarthogPgRepository(PumbaWarthogRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: PumbaWarthogQuery) -> PumbaWarthogResponse:
        logger.info(f"[PumbaWarthogPgRepository] introduce_myself 진입 | request_data={query}")
        return PumbaWarthogResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
