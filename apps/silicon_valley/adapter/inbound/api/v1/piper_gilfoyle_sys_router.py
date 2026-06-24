from fastapi import APIRouter, Depends

from silicon_valley.adapter.inbound.api.schemas.piper_gilfoyle_sys_schema import GilfoyleSysSchema
from silicon_valley.app.dtos.piper_gilfoyle_sys_dto import GilfoyleSysResponse
from silicon_valley.app.ports.input.piper_gilfoyle_sys_use_case import GilfoyleSysUseCase
from silicon_valley.dependencies.piper_gilfoyle_sys_provider import get_gilfoyle_sys_use_case

'''
버트람 길포일 (Bertram Gilfoyle)
파이드 파이퍼의 시스템·네트워크 아키텍트. 인프라와 서버를 도맡는 냉소적인 시스템 엔지니어로, 시스템 운영과 보안을 다루는 역할에 어울립니다.

추천 파일명: piper_gilfoyle_sys_router.py (Sys: 시스템 아키텍트)
'''
gilfoyle_router = APIRouter(prefix="/gilfoyle", tags=["gilfoyle"])

@gilfoyle_router.get("/myself")
async def introduce_myself(
    gilfoyle: GilfoyleSysUseCase = Depends(get_gilfoyle_sys_use_case)
) -> GilfoyleSysResponse :

    return await gilfoyle.introduce_myself(
        GilfoyleSysSchema(
            id=2,
            name="버트람 길포일 (Bertram Gilfoyle)"
        )
    )
