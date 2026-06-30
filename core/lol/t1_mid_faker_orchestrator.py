"""T1 미드 Faker 오케스트레이터.

LoL T1의 미드 캐리(Faker)가 경기를 지휘하듯, 등록된 LLM 모델을 받아
추론을 지휘하는 중앙 오케스트레이터. 현재 EXAONE 3.5 2.4B(Ollama)를
기본 모델로 등록한다.
"""
from __future__ import annotations

from dataclasses import dataclass

from ollama import AsyncClient


@dataclass(frozen=True)
class ModelSpec:
    """오케스트레이터에 등록되는 모델 명세."""

    name: str   # Ollama 모델 태그 (예: "exaone3.5:2.4b")
    label: str  # 사람이 읽는 이름


class T1MidFakerOrchestrator:
    """등록된 모델 중 하나를 골라 채팅 추론을 수행하는 오케스트레이터."""

    def __init__(self, host: str | None = None) -> None:
        self._client = AsyncClient(host=host) if host else AsyncClient()
        self._registry: dict[str, ModelSpec] = {}
        self._default: str | None = None

    def register(self, key: str, spec: ModelSpec, *, default: bool = False) -> None:
        """모델을 레지스트리에 등록한다. 첫 등록 모델은 자동으로 기본값이 된다."""
        self._registry[key] = spec
        if default or self._default is None:
            self._default = key

    async def orchestrate(self, prompt: str, *, model_key: str | None = None) -> str:
        """등록된 모델로 프롬프트를 추론한다. model_key 미지정 시 기본 모델 사용."""
        key = model_key or self._default
        if key is None:
            raise RuntimeError("등록된 모델이 없습니다. register()로 먼저 등록하세요.")

        spec = self._registry[key]
        response = await self._client.chat(
            model=spec.name,
            messages=[{"role": "user", "content": prompt}],
        )
        return response["message"]["content"]


# --- EXAONE 3.5 2.4B 등록 ---
EXAONE_3_5_2_4B = ModelSpec(name="exaone3.5:2.4b", label="EXAONE 3.5 2.4B")

orchestrator = T1MidFakerOrchestrator()
orchestrator.register("exaone", EXAONE_3_5_2_4B, default=True)


if __name__ == "__main__":
    import asyncio

    answer = asyncio.run(orchestrator.orchestrate("한국어로 짧게 자기소개 해줘."))
    print(answer)
