from fastapi import APIRouter, Depends

from sherlock_homes.adapter.inbound.api.schemas.detective_holmes_analyst_schema import HolmesAnalystSchema
from sherlock_homes.app.dtos.detective_holmes_analyst_dto import HolmesAnalystResponse
from sherlock_homes.app.ports.input.detective_holmes_analyst_use_case import HolmesAnalystUseCase
from sherlock_homes.dependencies.detective_holmes_analyst_provider import get_holmes_analyst_use_case

holmes_analyst_router = APIRouter(prefix="/holmes", tags=["holmes"])


@holmes_analyst_router.get("/myself")
async def introduce_myself(
    uc: HolmesAnalystUseCase = Depends(get_holmes_analyst_use_case)
) -> HolmesAnalystResponse:
    return await uc.introduce_myself(
        HolmesAnalystSchema(
            id=9,
            name="셜록 홈즈 (Sherlock)"
        )
    )
