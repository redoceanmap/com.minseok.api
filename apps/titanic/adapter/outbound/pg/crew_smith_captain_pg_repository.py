from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession
from titanic.app.dtos.crew_smith_captain_dto import SmithCaptainQuery, SmithCaptainResponse, ChatResponse

logger = logging.getLogger(__name__)

class SmithCaptainPgRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: SmithCaptainQuery) -> SmithCaptainResponse:
        '''스미스 선장의 자기 소개 레포지토리 구현 메소드'''

        logger.info(f"[SmithCaptainPgRepository] introduce_myself 진입 | request_data={query}")

        response: SmithCaptainResponse = SmithCaptainResponse(
            id= query.id * 10000,
            name= query.name + "가 레포지토리에 다녀옴"
        )
        return response

    async def chat(self, message: str) -> ChatResponse:
        logger.info(f"[SmithCaptainPgRepository] chat 진입 | message={message}")
        return ChatResponse(text=message)
