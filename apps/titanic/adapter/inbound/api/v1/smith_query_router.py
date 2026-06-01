import logging

from fastapi import APIRouter, HTTPException, Request

from backend.apps.titanic.app.ports.input.smith_query_use_case import SmithQueryUseCase

logger = logging.getLogger("smith.inbound.smith_query_router")

smith_query_router = APIRouter(prefix="/titanic/smith", tags=["smith-query"])


def _get_use_case(request: Request) -> SmithQueryUseCase:
    use_case: SmithQueryUseCase | None = getattr(request.app.state, "smith_query", None)
    if use_case is None:
        raise HTTPException(status_code=503, detail="smith_query가 초기화되지 않았습니다.")
    return use_case


@smith_query_router.get("/passengers")
async def get_passengers(request: Request):
    use_case = _get_use_case(request)
    return await use_case.get_passengers()
