from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from lion_king.app.dtos.outcast_scar_chatbot_dto import ScarChatbotQuery, ScarChatbotResponse
from lion_king.app.ports.output.outcast_scar_chatbot_repository import ScarChatbotRepository

logger = logging.getLogger(__name__)


class ScarChatbotPgRepository(ScarChatbotRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: ScarChatbotQuery) -> ScarChatbotResponse:
        logger.info(f"[ScarChatbotPgRepository] introduce_myself 진입 | request_data={query}")
        return ScarChatbotResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
