from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.app.dtos.detective_mrshudson_manager_dto import MrshudsonManagerQuery, MrshudsonManagerResponse
from sherlock_homes.app.ports.output.detective_mrshudson_manager_repository import MrshudsonManagerRepository

logger = logging.getLogger(__name__)


class MrshudsonManagerPgRepository(MrshudsonManagerRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: MrshudsonManagerQuery) -> MrshudsonManagerResponse:
        '''허드슨 부인 (Mrs. Hudson)의 자기 소개 레포지토리 구현 메소드'''
        logger.info(f"[MrshudsonManagerPgRepository] introduce_myself 진입 | request_data={query}")
        return MrshudsonManagerResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
