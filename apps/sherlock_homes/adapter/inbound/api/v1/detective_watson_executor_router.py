from fastapi import APIRouter, Depends

from sherlock_homes.adapter.inbound.api.schemas.detective_watson_executor_schema import WatsonExecutorSchema
from sherlock_homes.app.dtos.detective_watson_executor_dto import WatsonExecutorResponse
from sherlock_homes.app.ports.input.detective_watson_executor_use_case import WatsonExecutorUseCase
from sherlock_homes.dependencies.detective_watson_executor_provider import get_watson_executor_use_case

watson_executor_router = APIRouter(prefix="/watson", tags=["watson"])


@watson_executor_router.get("/myself")
async def introduce_myself(
    uc: WatsonExecutorUseCase = Depends(get_watson_executor_use_case)
) -> WatsonExecutorResponse:
    return await uc.introduce_myself(
        WatsonExecutorSchema(
            id=10,
            name="존 왓슨 (John)"
        )
    )
