import logging

from fastapi import APIRouter, HTTPException, Request

from backend.apps.titanic.app.ports.input.cal_query_use_case import CalQueryUseCase

logger = logging.getLogger(__name__)

cal_query_router = APIRouter(prefix="/titanic/cal", tags=["cal-query"])


def _get_use_case(request: Request) -> CalQueryUseCase:
    use_case: CalQueryUseCase | None = getattr(request.app.state, "cal_query", None)
    if use_case is None:
        raise HTTPException(status_code=503, detail="cal_query가 초기화되지 않았습니다.")
    return use_case


@cal_query_router.get("/passengers")
async def get_passengers(request: Request):
    use_case = _get_use_case(request)
    return await use_case.get_passengers()
