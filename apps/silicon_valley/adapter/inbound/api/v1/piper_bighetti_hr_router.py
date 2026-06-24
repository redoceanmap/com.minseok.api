from fastapi import APIRouter, Depends

from silicon_valley.adapter.inbound.api.schemas.piper_bighetti_hr_schema import BighettiHrSchema
from silicon_valley.app.dtos.piper_bighetti_hr_dto import BighettiHrResponse
from silicon_valley.app.ports.input.piper_bighetti_hr_use_case import BighettiHrUseCase
from silicon_valley.dependencies.piper_bighetti_hr_provider import get_bighetti_hr_use_case

'''
넬슨 '빅헤드' 비게티 (Nelson 'Big Head' Bighetti)
리처드의 오랜 친구. 별다른 노력 없이 얼떨결에 승진을 거듭하는 인물로, 사람·인사(HR) 영역을 다루는 역할에 어울립니다.

추천 파일명: piper_bighetti_hr_router.py (HR: 인사 담당)
'''
bighetti_router = APIRouter(prefix="/bighetti", tags=["bighetti"])

@bighetti_router.get("/myself")
async def introduce_myself(
    bighetti: BighettiHrUseCase = Depends(get_bighetti_hr_use_case)
) -> BighettiHrResponse :

    return await bighetti.introduce_myself(
        BighettiHrSchema(
            id=5,
            name="넬슨 '빅헤드' 비게티 (Nelson 'Big Head' Bighetti)"
        )
    )
