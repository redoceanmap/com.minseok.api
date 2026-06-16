from __future__ import annotations

from abc import ABC, abstractmethod

from sherlock_homes.app.dtos.detective_mary_operator_dto import MaryOperatorQuery, MaryOperatorResponse


class MaryOperatorRepository(ABC):

    @abstractmethod
    def introduce_myself(self, query: MaryOperatorQuery) -> MaryOperatorResponse:
        '''메리 왓슨 (Mary)의 자기 소개 레포지토리 추상 메소드'''
        pass
