import logging

from backend.apps.titanic.adapter.inbound.api.schemas.james_command_schema import TitanicPassengerRequestSchema
from backend.apps.titanic.app.ports.input.james_command_use_case import JamesCommandUseCase
from backend.apps.titanic.app.ports.output.james_command_repository import JamesCommandRepository

logger = logging.getLogger("james.app.james_command")


class JamesCommandInteractor(JamesCommandUseCase):

    def __init__(self, repository: JamesCommandRepository) -> None:
        self.repository = repository

    async def upload_passengers(self, passengers: list[TitanicPassengerRequestSchema]) -> dict:
        logger.info("승객 업로드 시작 (%d건)", len(passengers))
        await self.repository.save_passengers(passengers)
        logger.info("승객 업로드 완료 (%d건)", len(passengers))
        return {"count": len(passengers), "data": [p.model_dump() for p in passengers]}
    
    
