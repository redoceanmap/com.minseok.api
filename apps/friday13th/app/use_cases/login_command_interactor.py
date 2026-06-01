import logging
import bcrypt
from backend.apps.friday13th.domain.entities.user_entity import UserModel
from backend.apps.friday13th.app.ports.input.login_command_use_case import LoginCommandUseCasePort
from backend.apps.friday13th.app.ports.output.login_command_repository import LoginCommandRepositoryPort
from backend.apps.friday13th.adapter.inbound.api.schemas.user_schema import LoginSchema

logger = logging.getLogger(__name__)


def _verify_password(plain: str, stored: str) -> bool:
    if not stored:
        return False
    try:
        return bcrypt.checkpw(plain.encode("utf-8"), stored.encode("utf-8"))
    except (ValueError, TypeError):
        return False


def _hash_password(plain: str) -> str:
    return bcrypt.hashpw(plain.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


class LoginCommandInteractor(LoginCommandUseCasePort):

    def __init__(self, login_repository: LoginCommandRepositoryPort) -> None:
        self._login_repository = login_repository

    async def login_user(self, login_schema: LoginSchema) -> UserModel | None:
        user = await self._login_repository.find_by_email(login_schema.email)
        if user is None:
            logger.info("[LoginCommandInteractor] 실패 — 미가입 email=%s", login_schema.email)
            return None

        if _verify_password(login_schema.password, user.password):
            logger.info("[LoginCommandInteractor] 성공(해시) — email=%s", login_schema.email)
            return user

        if user.password == login_schema.password:
            new_hashed = _hash_password(login_schema.password)
            await self._login_repository.update_password(login_schema.email, new_hashed)
            logger.info("[LoginCommandInteractor] 성공(평문→해시 마이그레이션) — email=%s", login_schema.email)
            return user

        logger.info("[LoginCommandInteractor] 실패 — 비번 불일치 email=%s", login_schema.email)
        return None
