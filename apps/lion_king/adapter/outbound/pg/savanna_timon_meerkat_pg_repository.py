from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from lion_king.app.dtos.savanna_timon_meerkat_dto import TimonMeerkatQuery, TimonMeerkatResponse
from lion_king.app.ports.output.savanna_timon_meerkat_repository import TimonMeerkatRepository

logger = logging.getLogger(__name__)


class TimonMeerkatPgRepository(TimonMeerkatRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: TimonMeerkatQuery) -> TimonMeerkatResponse:
        logger.info(f"[TimonMeerkatPgRepository] introduce_myself 진입 | request_data={query}")
        return TimonMeerkatResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
