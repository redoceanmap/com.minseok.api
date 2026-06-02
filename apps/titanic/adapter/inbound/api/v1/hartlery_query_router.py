import logging

from fastapi import APIRouter, HTTPException, Request

from backend.apps.titanic.app.ports.input.hartlery_query_use_case import HartleryQueryUseCase

logger = logging.getLogger(__name__)

hartlery_query_router = APIRouter(prefix="/titanic/hartlery", tags=["hartlery-query"])


def _get_use_case(request: Request) -> HartleryQueryUseCase:
    use_case: HartleryQueryUseCase | None = getattr(request.app.state, "hartlery_query", None)
    if use_case is None:
        raise HTTPException(status_code=503, detail="hartlery_query가 초기화되지 않았습니다.")
    return use_case


@hartlery_query_router.get("/passengers")
async def get_passengers(request: Request):
    use_case = _get_use_case(request)
    return await use_case.get_passengers()
