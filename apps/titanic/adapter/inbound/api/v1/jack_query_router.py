import logging

from fastapi import APIRouter, HTTPException, Request

from backend.apps.titanic.app.ports.input.jack_query_use_case import JackQueryUseCase

logger = logging.getLogger("jack.inbound.jack_query_router")

jack_query_router = APIRouter(prefix="/titanic/jack", tags=["jack-query"])


def _get_use_case(request: Request) -> JackQueryUseCase:
    use_case: JackQueryUseCase | None = getattr(request.app.state, "jack_query", None)
    if use_case is None:
        raise HTTPException(status_code=503, detail="jack_query가 초기화되지 않았습니다.")
    return use_case


@jack_query_router.get("/passengers")
async def get_passengers(request: Request):
    use_case = _get_use_case(request)
    return await use_case.get_passengers()
