from fastapi import APIRouter, Depends

from sherlock_homes.adapter.inbound.api.schemas.criminal_moriarty_disruptor_schema import MoriartyDisruptorSchema
from sherlock_homes.app.dtos.criminal_moriarty_disruptor_dto import MoriartyDisruptorResponse
from sherlock_homes.app.ports.input.criminal_moriarty_disruptor_use_case import MoriartyDisruptorUseCase
from sherlock_homes.dependencies.criminal_moriarty_disruptor_provider import get_moriarty_disruptor_use_case

moriarty_disruptor_router = APIRouter(prefix="/moriarty", tags=["moriarty"])


@moriarty_disruptor_router.get("/myself")
async def introduce_myself(
    uc: MoriartyDisruptorUseCase = Depends(get_moriarty_disruptor_use_case)
) -> MoriartyDisruptorResponse:
    return await uc.introduce_myself(
        MoriartyDisruptorSchema(
            id=5,
            name="모리어티 (Moriarty)"
        )
    )
