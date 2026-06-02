import logging

from fastapi import APIRouter, HTTPException, Request

from backend.apps.titanic.app.ports.input.andrews_query_use_case import AndrewsQueryUseCase

logger = logging.getLogger(__name__)

andrews_query_router = APIRouter(prefix="/titanic/andrews", tags=["andrews-query"])


def _get_use_case(request: Request) -> AndrewsQueryUseCase:
    use_case: AndrewsQueryUseCase | None = getattr(request.app.state, "andrews_query", None)
    if use_case is None:
        raise HTTPException(status_code=503, detail="andrews_query가 초기화되지 않았습니다.")
    return use_case


@andrews_query_router.get("/passengers")
async def get_passengers(request: Request):
    use_case = _get_use_case(request)
    return await use_case.get_passengers()
