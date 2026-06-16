from fastapi import APIRouter, Depends

from sherlock_homes.adapter.inbound.api.schemas.detective_mrshudson_manager_schema import MrshudsonManagerSchema
from sherlock_homes.app.dtos.detective_mrshudson_manager_dto import MrshudsonManagerResponse
from sherlock_homes.app.ports.input.detective_mrshudson_manager_use_case import MrshudsonManagerUseCase
from sherlock_homes.dependencies.detective_mrshudson_manager_provider import get_mrshudson_manager_use_case

mrshudson_manager_router = APIRouter(prefix="/mrshudson", tags=["mrshudson"])


@mrshudson_manager_router.get("/myself")
async def introduce_myself(
    uc: MrshudsonManagerUseCase = Depends(get_mrshudson_manager_use_case)
) -> MrshudsonManagerResponse:
    return await uc.introduce_myself(
        MrshudsonManagerSchema(
            id=11,
            name="허드슨 부인 (Mrs. Hudson)"
        )
    )
