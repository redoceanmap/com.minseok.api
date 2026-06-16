from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from lion_king.app.dtos.pride_mufasa_news_dto import MufasaNewsQuery, MufasaNewsResponse
from lion_king.app.ports.output.pride_mufasa_news_repository import MufasaNewsRepository

logger = logging.getLogger(__name__)


class MufasaNewsPgRepository(MufasaNewsRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: MufasaNewsQuery) -> MufasaNewsResponse:
        logger.info(f"[MufasaNewsPgRepository] introduce_myself 진입 | request_data={query}")
        return MufasaNewsResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
