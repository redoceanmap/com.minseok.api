from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from lion_king.app.dtos.outcast_shenzi_pack_dto import ShenziPackQuery, ShenziPackResponse
from lion_king.app.ports.output.outcast_shenzi_pack_repository import ShenziPackRepository

logger = logging.getLogger(__name__)


class ShenziPackPgRepository(ShenziPackRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: ShenziPackQuery) -> ShenziPackResponse:
        logger.info(f"[ShenziPackPgRepository] introduce_myself 진입 | request_data={query}")
        return ShenziPackResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
