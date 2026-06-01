import logging

from fastapi import APIRouter, HTTPException, Request

from backend.apps.titanic.app.ports.input.isidor_query_use_case import IsidorQueryUseCase

logger = logging.getLogger("isidor.inbound.isidor_query_router")

isidor_query_router = APIRouter(prefix="/titanic/isidor", tags=["isidor-query"])


def _get_use_case(request: Request) -> IsidorQueryUseCase:
    use_case: IsidorQueryUseCase | None = getattr(request.app.state, "isidor_query", None)
    if use_case is None:
        raise HTTPException(status_code=503, detail="isidor_query가 초기화되지 않았습니다.")
    return use_case


@isidor_query_router.get("/passengers")
async def get_passengers(request: Request):
    use_case = _get_use_case(request)
    return await use_case.get_passengers()
