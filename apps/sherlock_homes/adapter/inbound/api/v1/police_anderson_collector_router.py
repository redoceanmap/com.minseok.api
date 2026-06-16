from fastapi import APIRouter, Depends

from sherlock_homes.adapter.inbound.api.schemas.police_anderson_collector_schema import AndersonCollectorSchema
from sherlock_homes.app.dtos.police_anderson_collector_dto import AndersonCollectorResponse
from sherlock_homes.app.ports.input.police_anderson_collector_use_case import AndersonCollectorUseCase
from sherlock_homes.dependencies.police_anderson_collector_provider import get_anderson_collector_use_case

anderson_collector_router = APIRouter(prefix="/anderson", tags=["anderson"])


@anderson_collector_router.get("/myself")
async def introduce_myself(
    uc: AndersonCollectorUseCase = Depends(get_anderson_collector_use_case)
) -> AndersonCollectorResponse:
    return await uc.introduce_myself(
        AndersonCollectorSchema(
            id=2,
            name="앤더슨 (Anderson)"
        )
    )
