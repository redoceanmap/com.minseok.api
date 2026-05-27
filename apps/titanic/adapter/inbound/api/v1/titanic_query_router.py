from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from titanic.app.ports.input.titanic_query_port import TitanicQueryPort
from backend.apps.titanic.app.use_cases.train_use_case import JackService
from titanic.app.use_cases.titanic_query_impl import TitanicQueryImpl

titanic_router = APIRouter(prefix="/titanic", tags=["titanic-query"])


def _get_query_port(request: Request) -> TitanicQueryPort:
    jack: JackService | None = request.app.state.jack
    if jack is None:
        raise HTTPException(status_code=503, detail="데이터가 없습니다. CSV를 먼저 업로드해주세요.")
    return TitanicQueryImpl(jack)


@titanic_router.get("/data")
async def read_titanic_data(
    request: Request, db: AsyncSession = Depends(get_db)
):
    query_port = _get_query_port(request)
    return await query_port.get_data(db)


@titanic_router.get("/count")
async def read_titanic_count(
    request: Request, db: AsyncSession = Depends(get_db)
):
    query_port = _get_query_port(request)
    return {"count": await query_port.get_count(db)}


@titanic_router.get("/tree")
async def read_titanic_tree(request: Request):
    query_port = _get_query_port(request)
    return {"tree": query_port.get_tree()}


@titanic_router.get("/model")
async def read_titanic_model(request: Request):
    query_port = _get_query_port(request)
    return {"model": query_port.get_model_name(), "accuracy": query_port.get_accuracy()}


@titanic_router.get("/count/survived")
async def read_titanic_count_survived(
    request: Request, db: AsyncSession = Depends(get_db)
):
    query_port = _get_query_port(request)
    return {"survived": await query_port.get_survived(db)}


@titanic_router.get("/count/dead")
async def read_titanic_count_dead(
    request: Request, db: AsyncSession = Depends(get_db)
):
    query_port = _get_query_port(request)
    return {"dead": await query_port.get_dead(db)}
