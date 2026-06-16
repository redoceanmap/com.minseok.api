from fastapi import APIRouter, Depends

from sherlock_homes.adapter.inbound.api.schemas.criminal_irene_ilustrator_schema import IreneIlustratorSchema
from sherlock_homes.app.dtos.criminal_irene_ilustrator_dto import IreneIlustratorResponse
from sherlock_homes.app.ports.input.criminal_irene_ilustrator_use_case import IreneIlustratorUseCase
from sherlock_homes.dependencies.criminal_irene_ilustrator_provider import get_irene_ilustrator_use_case

irene_ilustrator_router = APIRouter(prefix="/irene", tags=["irene"])


@irene_ilustrator_router.get("/myself")
async def introduce_myself(
    uc: IreneIlustratorUseCase = Depends(get_irene_ilustrator_use_case)
) -> IreneIlustratorResponse:
    return await uc.introduce_myself(
        IreneIlustratorSchema(
            id=7,
            name="아이린 애들러 (Irene)"
        )
    )
