import logging
from fastapi import APIRouter, HTTPException, Request
from backend.apps.titanic.app.ports.input.passenger_query_use_case import PassengerQueryUseCasePort

logger = logging.getLogger(__name__)

passenger_query_router = APIRouter(prefix="/titanic/passenger", tags=["passenger-query"])


def _get_use_case(request: Request) -> PassengerQueryUseCasePort:
    use_case: PassengerQueryUseCasePort | None = getattr(request.app.state, "passenger_query_interactor", None)
    if use_case is None:
        raise HTTPException(status_code=503, detail="passenger_query_interactor가 초기화되지 않았습니다.")
    return use_case


@passenger_query_router.get("/count")
async def get_count(request: Request):
    logger.info("[QUERY] 승객 수 조회 요청")
    count = await _get_use_case(request).get_count()
    logger.info("[QUERY] 승객 수 조회 완료 — %d명", count)
    return {"count": count}


@passenger_query_router.get("/count/survived")
async def get_survived(request: Request):
    logger.info("[QUERY] 생존자 수 조회 요청")
    survived = await _get_use_case(request).get_survived()
    logger.info("[QUERY] 생존자 수 조회 완료 — %d명", survived)
    return {"survived": survived}


@passenger_query_router.get("/count/dead")
async def get_dead(request: Request):
    logger.info("[QUERY] 사망자 수 조회 요청")
    dead = await _get_use_case(request).get_dead()
    logger.info("[QUERY] 사망자 수 조회 완료 — %d명", dead)
    return {"dead": dead}
