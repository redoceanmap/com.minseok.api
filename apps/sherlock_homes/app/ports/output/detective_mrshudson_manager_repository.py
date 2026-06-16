from __future__ import annotations

from abc import ABC, abstractmethod

from sherlock_homes.app.dtos.detective_mrshudson_manager_dto import MrshudsonManagerQuery, MrshudsonManagerResponse


class MrshudsonManagerRepository(ABC):

    @abstractmethod
    def introduce_myself(self, query: MrshudsonManagerQuery) -> MrshudsonManagerResponse:
        '''허드슨 부인 (Mrs. Hudson)의 자기 소개 레포지토리 추상 메소드'''
        pass
