from __future__ import annotations

# sherlock_router는 main.py에서 처음 접근할 때 지연 생성됩니다. (PEP 562)

_sherlock_router = None


def __getattr__(name: str):
    global _sherlock_router

    if name == "sherlock_router":
        if _sherlock_router is None:
            _sherlock_router = _build_sherlock_router()
        return _sherlock_router

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def _build_sherlock_router():
    from fastapi import APIRouter

    from sherlock_homes.adapter.inbound.api.v1.detective_watson_executor_router import watson_executor_router

    router = APIRouter(prefix="/sherlock", tags=["sherlock"])
    router.include_router(watson_executor_router)
    return router
