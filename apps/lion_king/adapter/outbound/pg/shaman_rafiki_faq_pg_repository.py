from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from lion_king.app.dtos.shaman_rafiki_faq_dto import RafikiFaqQuery, RafikiFaqResponse
from lion_king.app.ports.output.shaman_rafiki_faq_repository import RafikiFaqRepository

logger = logging.getLogger(__name__)


class RafikiFaqPgRepository(RafikiFaqRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: RafikiFaqQuery) -> RafikiFaqResponse:
        logger.info(f"[RafikiFaqPgRepository] introduce_myself 진입 | request_data={query}")
        return RafikiFaqResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
