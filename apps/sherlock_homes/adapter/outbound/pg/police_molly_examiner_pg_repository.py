from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.app.dtos.police_molly_examiner_dto import MollyExaminerQuery, MollyExaminerResponse
from sherlock_homes.app.ports.output.police_molly_examiner_repository import MollyExaminerRepository

logger = logging.getLogger(__name__)


class MollyExaminerPgRepository(MollyExaminerRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: MollyExaminerQuery) -> MollyExaminerResponse:
        '''몰리 후퍼의 자기 소개 레포지토리 구현 메소드'''
        logger.info(f"[MollyExaminerPgRepository] introduce_myself 진입 | request_data={query}")
        return MollyExaminerResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
