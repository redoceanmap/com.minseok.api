from __future__ import annotations

from core.lol.t1_mid_faker_orchestrator import orchestrator
from sherlock_homes.app.dtos.detective_watson_executor_dto import DispatchCommand, DispatchResult
from sherlock_homes.app.ports.input.detective_watson_executor_use_case import WatsonExecutorUseCase
from sherlock_homes.app.ports.output.detective_watson_executor_port import WatsonExecutorPort


class WatsonExecutorInteractor(WatsonExecutorUseCase):

    def __init__(self, port: WatsonExecutorPort) -> None:
        self._port = port

    async def dispatch(self, command: DispatchCommand) -> DispatchResult:
        body = await orchestrator.orchestrate(
            f"다음 주제로 이메일 본문을 한국어로 작성해줘. 인사말과 맺음말을 포함해. 주제: {command.topic}"
        )
        subject = await orchestrator.orchestrate(
            f"다음 이메일 본문에 어울리는 제목을 따옴표 없이 한 줄로만 작성해줘:\n\n{body}"
        )
        result = await self._port.send(command.to_email, subject.strip(), body)
        return DispatchResult(status="sent", detail=str(result))
