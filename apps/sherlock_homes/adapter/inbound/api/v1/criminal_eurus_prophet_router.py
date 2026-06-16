from fastapi import APIRouter, Depends

from sherlock_homes.adapter.inbound.api.schemas.criminal_eurus_prophet_schema import EurusProphetSchema
from sherlock_homes.app.dtos.criminal_eurus_prophet_dto import EurusProphetResponse
from sherlock_homes.app.ports.input.criminal_eurus_prophet_use_case import EurusProphetUseCase
from sherlock_homes.dependencies.criminal_eurus_prophet_provider import get_eurus_prophet_use_case

eurus_prophet_router = APIRouter(prefix="/eurus", tags=["eurus"])


@eurus_prophet_router.get("/myself")
async def introduce_myself(
    uc: EurusProphetUseCase = Depends(get_eurus_prophet_use_case)
) -> EurusProphetResponse:
    return await uc.introduce_myself(
        EurusProphetSchema(
            id=6,
            name="유라루스 홈즈 (Eurus)"
        )
    )
