from __future__ import annotations

from abc import ABC, abstractmethod

from sherlock_homes.app.dtos.detective_watson_executor_dto import WatsonExecutorQuery, WatsonExecutorResponse


class WatsonExecutorRepository(ABC):

    @abstractmethod
    def introduce_myself(self, query: WatsonExecutorQuery) -> WatsonExecutorResponse:
        '''존 왓슨 (John)의 자기 소개 레포지토리 추상 메소드'''
        pass
