from fastapi import APIRouter, Depends

from sherlock_homes.adapter.inbound.api.schemas.criminal_magnussen_archivist_schema import MagnussenArchivistSchema
from sherlock_homes.app.dtos.criminal_magnussen_archivist_dto import MagnussenArchivistResponse
from sherlock_homes.app.ports.input.criminal_magnussen_archivist_use_case import MagnussenArchivistUseCase
from sherlock_homes.dependencies.criminal_magnussen_archivist_provider import get_magnussen_archivist_use_case

magnussen_archivist_router = APIRouter(prefix="/magnussen", tags=["magnussen"])


@magnussen_archivist_router.get("/myself")
async def introduce_myself(
    uc: MagnussenArchivistUseCase = Depends(get_magnussen_archivist_use_case)
) -> MagnussenArchivistResponse:
    return await uc.introduce_myself(
        MagnussenArchivistSchema(
            id=8,
            name="마그누센 (Magnussen)"
        )
    )
