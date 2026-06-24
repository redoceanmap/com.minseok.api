from __future__ import annotations

from abc import ABC, abstractmethod

from sherlock_homes.adapter.inbound.api.schemas.detective_watson_executor_dto import WatsonExecutorDto
from sherlock_homes.app.dtos.detective_watson_executor_dto import WatsonExecutorResponse


class WatsonExecutorUseCase(ABC):

    @abstractmethod
    async def introduce_myself(self, schema: WatsonExecutorDto) -> WatsonExecutorResponse:
        '''존 왓슨의 자기소개 메소드'''
        pass
