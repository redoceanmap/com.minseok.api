from fastapi import APIRouter, Depends

from sherlock_homes.adapter.inbound.api.schemas.police_mycroft_libraraian_schema import MycroftLibraraianSchema
from sherlock_homes.app.dtos.police_mycroft_libraraian_dto import MycroftLibraraianResponse
from sherlock_homes.app.ports.input.police_mycroft_libraraian_use_case import MycroftLibraraianUseCase
from sherlock_homes.dependencies.police_mycroft_libraraian_provider import get_mycroft_libraraian_use_case

mycroft_libraraian_router = APIRouter(prefix="/mycroft", tags=["mycroft"])


@mycroft_libraraian_router.get("/myself")
async def introduce_myself(
    uc: MycroftLibraraianUseCase = Depends(get_mycroft_libraraian_use_case)
) -> MycroftLibraraianResponse:
    return await uc.introduce_myself(
        MycroftLibraraianSchema(
            id=3,
            name="마이크로프트 홈즈 (Mycroft)"
        )
    )
