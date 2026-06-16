from __future__ import annotations

import logging

from sqlalchemy.ext.asyncio import AsyncSession

from lion_king.app.dtos.pride_sarabi_guardian_dto import SarabiGuardianQuery, SarabiGuardianResponse
from lion_king.app.ports.output.pride_sarabi_guardian_repository import SarabiGuardianRepository

logger = logging.getLogger(__name__)


class SarabiGuardianPgRepository(SarabiGuardianRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def introduce_myself(self, query: SarabiGuardianQuery) -> SarabiGuardianResponse:
        logger.info(f"[SarabiGuardianPgRepository] introduce_myself 진입 | request_data={query}")
        return SarabiGuardianResponse(
            id=query.id * 10000,
            name=query.name + "가 레포지토리에 다녀옴"
        )
