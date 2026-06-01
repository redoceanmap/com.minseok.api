import logging
from backend.apps.friday13th.app.ports.input.signup_query_use_case import SignupQueryUseCasePort
from backend.apps.friday13th.app.ports.output.signup_query_repository import SignupQueryRepositoryPort

logger = logging.getLogger(__name__)


class SignupQueryInteractor(SignupQueryUseCasePort):

    def __init__(self, signup_query_repository: SignupQueryRepositoryPort) -> None:
        self._signup_query_repository = signup_query_repository

    async def is_email_available(self, email: str) -> bool:
        user = await self._signup_query_repository.find_by_email(email)
        logger.info("[SignupQueryInteractor] 이메일 중복 확인 — email=%s, available=%s", email, user is None)
        return user is None
