from fastapi import APIRouter, Depends

from silicon_valley.adapter.inbound.api.schemas.piper_hendricks_ceo_schema import HendricksCeoSchema
from silicon_valley.app.dtos.piper_hendricks_ceo_dto import HendricksCeoResponse
from silicon_valley.app.ports.input.piper_hendricks_ceo_use_case import HendricksCeoUseCase
from silicon_valley.dependencies.piper_hendricks_ceo_provider import get_hendricks_ceo_use_case

'''
리처드 헨드릭스 (Richard Hendricks)
파이드 파이퍼(Pied Piper)의 창업자이자 CEO. 혁신적인 미들아웃 압축 알고리즘을 만든 천재 개발자로, 회사의 비전과 핵심 의사결정을 책임지는 역할입니다.

추천 파일명: piper_hendricks_ceo_router.py (CEO: 파이드 파이퍼 창업자)
'''
hendricks_router = APIRouter(prefix="/hendricks", tags=["hendricks"])

@hendricks_router.get("/myself")
async def introduce_myself(
    hendricks: HendricksCeoUseCase = Depends(get_hendricks_ceo_use_case)
) -> HendricksCeoResponse :

    return await hendricks.introduce_myself(
        HendricksCeoSchema(
            id=1,
            name="리처드 헨드릭스 (Richard Hendricks)"
        )
    )
