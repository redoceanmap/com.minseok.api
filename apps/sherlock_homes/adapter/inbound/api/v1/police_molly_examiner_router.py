from fastapi import APIRouter, Depends

from sherlock_homes.adapter.inbound.api.schemas.police_molly_examiner_schema import MollyExaminerSchema
from sherlock_homes.app.dtos.police_molly_examiner_dto import MollyExaminerResponse
from sherlock_homes.app.ports.input.police_molly_examiner_use_case import MollyExaminerUseCase
from sherlock_homes.dependencies.police_molly_examiner_provider import get_molly_examiner_use_case

molly_examiner_router = APIRouter(prefix="/molly", tags=["molly"])


@molly_examiner_router.get("/myself")
async def introduce_myself(
    uc: MollyExaminerUseCase = Depends(get_molly_examiner_use_case)
) -> MollyExaminerResponse:
    return await uc.introduce_myself(
        MollyExaminerSchema(
            id=4,
            name="몰리 후퍼 (Molly)"
        )
    )
