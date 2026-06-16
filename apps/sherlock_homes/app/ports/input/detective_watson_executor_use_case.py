from __future__ import annotations

from abc import ABC, abstractmethod

from sherlock_homes.adapter.inbound.api.schemas.detective_watson_executor_schema import WatsonExecutorSchema
from sherlock_homes.app.dtos.detective_watson_executor_dto import WatsonExecutorResponse


class WatsonExecutorUseCase(ABC):

    @abstractmethod
    async def introduce_myself(self, schema: WatsonExecutorSchema) -> WatsonExecutorResponse:
        '''존 왓슨 (John)의 자기소개 메소드'''
        pass
