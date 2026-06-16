from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.app.dtos.police_mycroft_libraraian_dto import MycroftLibraraianQuery, MycroftLibraraianResponse
from sherlock_homes.app.ports.output.police_mycroft_libraraian_repository import MycroftLibraraianRepository

logger = logging.getLogger(__name__)


class MycroftLibraraianPgRepository(MycroftLibraraianRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: MycroftLibraraianQuery) -> MycroftLibraraianResponse:
        '''마이크로프트 홈즈 (Mycroft)의 자기 소개 레포지토리 구현 메소드'''
        logger.info(f"[MycroftLibraraianPgRepository] introduce_myself 진입 | request_data={query}")
        return MycroftLibraraianResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
