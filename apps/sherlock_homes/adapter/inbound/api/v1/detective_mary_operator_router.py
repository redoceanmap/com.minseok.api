from fastapi import APIRouter, Depends

from sherlock_homes.adapter.inbound.api.schemas.detective_mary_operator_schema import MaryOperatorSchema
from sherlock_homes.app.dtos.detective_mary_operator_dto import MaryOperatorResponse
from sherlock_homes.app.ports.input.detective_mary_operator_use_case import MaryOperatorUseCase
from sherlock_homes.dependencies.detective_mary_operator_provider import get_mary_operator_use_case

mary_operator_router = APIRouter(prefix="/mary", tags=["mary"])


@mary_operator_router.get("/myself")
async def introduce_myself(
    uc: MaryOperatorUseCase = Depends(get_mary_operator_use_case)
) -> MaryOperatorResponse:
    return await uc.introduce_myself(
        MaryOperatorSchema(
            id=12,
            name="메리 왓슨 (Mary)"
        )
    )
