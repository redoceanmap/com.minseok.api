from __future__ import annotations

from abc import ABC, abstractmethod

from silicon_valley.app.dtos.piper_hendricks_ceo_dto import HendricksCeoQuery, HendricksCeoResponse


class HendricksCeoPort(ABC):

    @abstractmethod
    def introduce_myself(self, query: HendricksCeoQuery) -> HendricksCeoResponse:
        '''헨드릭스 CEO의 자기소개 레포지토리 추상 메소드'''
        pass
