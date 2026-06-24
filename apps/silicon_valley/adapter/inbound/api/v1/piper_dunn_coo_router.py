from fastapi import APIRouter, Depends

from silicon_valley.adapter.inbound.api.schemas.piper_dunn_coo_schema import DunnCooSchema
from silicon_valley.app.dtos.piper_dunn_coo_dto import DunnCooResponse
from silicon_valley.app.ports.input.piper_dunn_coo_use_case import DunnCooUseCase
from silicon_valley.dependencies.piper_dunn_coo_provider import get_dunn_coo_use_case

'''
도널드 '자레드' 던 (Donald 'Jared' Dunn)
파이드 파이퍼의 COO. 회사의 운영과 살림을 묵묵히 도맡는 헌신적인 비즈니스 책임자로, 운영·관리 흐름을 다루는 역할에 어울립니다.

추천 파일명: piper_dunn_coo_router.py (COO: 운영 책임자)
'''
dunn_router = APIRouter(prefix="/dunn", tags=["dunn"])

@dunn_router.get("/myself")
async def introduce_myself(
    dunn: DunnCooUseCase = Depends(get_dunn_coo_use_case)
) -> DunnCooResponse :

    return await dunn.introduce_myself(
        DunnCooSchema(
            id=4,
            name="도널드 '자레드' 던 (Donald 'Jared' Dunn)"
        )
    )
