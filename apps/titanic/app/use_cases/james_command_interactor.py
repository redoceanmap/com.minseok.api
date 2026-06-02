import dataclasses
import logging

from backend.apps.titanic.app.dtos.james_dto import PersonCommand, BookingCommand
from backend.apps.titanic.app.ports.input.james_command_use_case import JamesCommandUseCase
from backend.apps.titanic.app.ports.output.james_command_repository import JamesCommandRepository

logger = logging.getLogger(__name__)


class JamesCommandInteractor(JamesCommandUseCase):

    def __init__(self, repository: JamesCommandRepository) -> None:
        self.repository = repository

    async def upload_passengers(self, persons: list[PersonCommand], bookings: list[BookingCommand]) -> dict:
        logger.info("승객 업로드 시작 (%d건)", len(persons))
        preview = [dataclasses.asdict(p) for p in persons[:5]]
        logger.info("[제임스 유스케이스] 파싱된 상위 5개 레코드: %s", preview)
        await self.repository.save_passengers(persons, bookings)
        logger.info("승객 업로드 완료 (%d건)", len(persons))
        return {"count": len(persons)}
