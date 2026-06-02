import logging

from fastapi import APIRouter, HTTPException, Request

from backend.apps.titanic.app.ports.input.walter_query_use_case import WalterQueryUseCase

logger = logging.getLogger(__name__)

walter_query_router = APIRouter(prefix="/titanic/walter", tags=["walter-query"])


def _get_use_case(request: Request) -> WalterQueryUseCase:
    use_case: WalterQueryUseCase | None = getattr(request.app.state, "walter_query", None)
    if use_case is None:
        raise HTTPException(status_code=503, detail="walter_query가 초기화되지 않았습니다.")
    return use_case


@walter_query_router.get("/passengers")
async def get_passengers(request: Request):
    logger.info("요청 수신")
    use_case = _get_use_case(request)
    result = await use_case.get_passengers()
    logger.info("응답 반환 (%d건)", len(result))
    return result
