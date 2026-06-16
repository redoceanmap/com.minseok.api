from __future__ import annotations

from abc import ABC, abstractmethod

from sherlock_homes.adapter.inbound.api.schemas.detective_holmes_analyst_schema import HolmesAnalystSchema
from sherlock_homes.app.dtos.detective_holmes_analyst_dto import HolmesAnalystResponse


class HolmesAnalystUseCase(ABC):

    @abstractmethod
    async def introduce_myself(self, schema: HolmesAnalystSchema) -> HolmesAnalystResponse:
        '''셜록 홈즈 (Sherlock)의 자기소개 메소드'''
        pass
