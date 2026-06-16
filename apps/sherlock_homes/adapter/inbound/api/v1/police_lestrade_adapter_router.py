from fastapi import APIRouter, Depends

from sherlock_homes.adapter.inbound.api.schemas.police_lestrade_adapter_schema import LestradeAdapterSchema
from sherlock_homes.app.dtos.police_lestrade_adapter_dto import LestradeAdapterResponse
from sherlock_homes.app.ports.input.police_lestrade_adapter_use_case import LestradeAdapterUseCase
from sherlock_homes.dependencies.police_lestrade_adapter_provider import get_lestrade_adapter_use_case

lestrade_adapter_router = APIRouter(prefix="/lestrade", tags=["lestrade"])


@lestrade_adapter_router.get("/myself")
async def introduce_myself(
    uc: LestradeAdapterUseCase = Depends(get_lestrade_adapter_use_case)
) -> LestradeAdapterResponse:
    return await uc.introduce_myself(
        LestradeAdapterSchema(
            id=1,
            name="레스트레이드 경감 (Lestrade)"
        )
    )
