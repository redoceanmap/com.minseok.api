from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from sherlock_homes.app.dtos.criminal_magnussen_archivist_dto import MagnussenArchivistQuery, MagnussenArchivistResponse
from sherlock_homes.app.ports.output.criminal_magnussen_archivist_repository import MagnussenArchivistRepository

logger = logging.getLogger(__name__)


class MagnussenArchivistPgRepository(MagnussenArchivistRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: MagnussenArchivistQuery) -> MagnussenArchivistResponse:
        '''마그누센의 자기 소개 레포지토리 구현 메소드'''
        logger.info(f"[MagnussenArchivistPgRepository] introduce_myself 진입 | request_data={query}")
        return MagnussenArchivistResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
