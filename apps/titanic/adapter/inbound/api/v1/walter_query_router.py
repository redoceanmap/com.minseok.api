from fastapi import APIRouter
from backend.apps.titanic.adapter.inbound.api.schemas.walter_query_schema import WalterIntroduceSchema
from backend.apps.titanic.app.ports.input.walter_query_use_case import WalterQueryUseCase 
from backend.apps.titanic.app.use_cases.walter_query_interactor import WalterQueryInteractor

walter_query_router = APIRouter(prefix="/titanic/walter", tags=["walter-query"])

@walter_query_router.get("/myself")
async def introduce_myself():
    schema = WalterIntroduceSchema()
    pass

