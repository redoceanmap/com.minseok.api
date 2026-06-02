import logging

from backend.apps.titanic.app.ports.input.walter_query_use_case import WalterQueryUseCase
from backend.apps.titanic.app.ports.output.walter_query_repository import WalterQueryRepository

logger = logging.getLogger(__name__)


class WalterQueryInteractor(WalterQueryUseCase):

    def __init__(self, repository: WalterQueryRepository) -> None:
        self.repository = repository

    async def get_passengers(self) -> list[dict]:
        logger.info("승객 목록 조회 시작")
        result = await self.repository.get_all_passengers()
        logger.info("승객 목록 조회 완료 (%d건)", len(result))
        return result
