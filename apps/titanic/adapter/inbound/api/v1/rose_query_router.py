import logging

from fastapi import APIRouter, HTTPException, Request

from backend.apps.titanic.app.ports.input.model_query_use_case import ModelQueryUseCasePort
from backend.apps.titanic.app.use_cases.train_interactor import JackService
from backend.apps.titanic.app.use_cases.model_query_interactor import ModelQueryInteractor
from backend.apps.titanic.adapter.outbound.model_query_adapter import ModelQueryAdapter

logger = logging.getLogger("rose.inbound.rose_query_router")

rose_query_router = APIRouter(prefix="/titanic/rose", tags=["rose-query"])


def _get_use_case(request: Request) -> ModelQueryUseCasePort:
    jack: JackService | None = request.app.state.jack
    if jack is None:
        raise HTTPException(status_code=503, detail="데이터가 없습니다. CSV를 먼저 업로드해주세요.")
    return ModelQueryInteractor(ModelQueryAdapter(jack))


@rose_query_router.get("/info")
async def get_model_info(request: Request):
    logger.info("[QUERY] Rose 모델 정보 조회 요청")
    use_case = _get_use_case(request)
    model = use_case.get_model_name()
    accuracy = use_case.get_accuracy()
    logger.info("[QUERY] Rose 모델 정보 조회 완료 — model: %s, accuracy: %.4f", model, accuracy)
    return {"model": model, "accuracy": accuracy}


@rose_query_router.get("/tree")
async def get_tree(request: Request):
    logger.info("[QUERY] Rose 의사결정 트리 조회 요청")
    use_case = _get_use_case(request)
    return {"tree": use_case.get_tree()}
