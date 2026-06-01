import logging
import bcrypt
from backend.apps.friday13th.domain.entities.user_entity import UserModel
from backend.apps.friday13th.app.ports.input.signup_command_use_case import SignupCommandUseCasePort
from backend.apps.friday13th.app.ports.output.signup_command_repository import SignupCommandRepositoryPort
from backend.apps.friday13th.adapter.inbound.api.schemas.user_schema import UserSchema

logger = logging.getLogger(__name__)


def _hash_password(plain: str) -> str:
    return bcrypt.hashpw(plain.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


class SignupCommandInteractor(SignupCommandUseCasePort):

    def __init__(self, signup_repository: SignupCommandRepositoryPort) -> None:
        self._signup_repository = signup_repository

    async def save_user(self, user_schema: UserSchema) -> UserModel:
        hashed = user_schema.model_copy(update={"password": _hash_password(user_schema.password)})
        user = await self._signup_repository.save_user(hashed)
        logger.info("[SignupCommandInteractor] save_user 완료 — userId=%s", user.user_id)
        return user
