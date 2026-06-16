from __future__ import annotations

from abc import ABC, abstractmethod

from sherlock_homes.adapter.inbound.api.schemas.detective_mrshudson_manager_schema import MrshudsonManagerSchema
from sherlock_homes.app.dtos.detective_mrshudson_manager_dto import MrshudsonManagerResponse


class MrshudsonManagerUseCase(ABC):

    @abstractmethod
    async def introduce_myself(self, schema: MrshudsonManagerSchema) -> MrshudsonManagerResponse:
        '''허드슨 부인 (Mrs. Hudson)의 자기소개 메소드'''
        pass
