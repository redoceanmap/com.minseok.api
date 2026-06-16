from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from lion_king.app.dtos.savanna_zazu_hornbill_dto import ZazuHornbillQuery, ZazuHornbillResponse
from lion_king.app.ports.output.savanna_zazu_hornbill_repository import ZazuHornbillRepository

logger = logging.getLogger(__name__)


class ZazuHornbillPgRepository(ZazuHornbillRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: ZazuHornbillQuery) -> ZazuHornbillResponse:
        logger.info(f"[ZazuHornbillPgRepository] introduce_myself 진입 | request_data={query}")
        return ZazuHornbillResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
