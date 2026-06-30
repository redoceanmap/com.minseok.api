from __future__ import annotations

from abc import ABC, abstractmethod


class WatsonExecutorPort(ABC):

    @abstractmethod
    async def send(self, to_email: str, subject: str, body: str) -> dict:
        '''완성된 제목·본문을 외부 발송 채널(n8n/Gmail)로 전달한다.'''
        ...
