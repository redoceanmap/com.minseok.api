import logging

from fastapi import APIRouter, HTTPException, Request

from backend.apps.titanic.app.ports.input.ruth_query_use_case import RuthQueryUseCase

logger = logging.getLogger("ruth.inbound.ruth_query_router")

ruth_query_router = APIRouter(prefix="/titanic/ruth", tags=["ruth-query"])


def _get_use_case(request: Request) -> RuthQueryUseCase:
    use_case: RuthQueryUseCase | None = getattr(request.app.state, "ruth_query", None)
    if use_case is None:
        raise HTTPException(status_code=503, detail="ruth_query가 초기화되지 않았습니다.")
    return use_case


@ruth_query_router.get("/passengers")
async def get_passengers(request: Request):
    use_case = _get_use_case(request)
    return await use_case.get_passengers()
