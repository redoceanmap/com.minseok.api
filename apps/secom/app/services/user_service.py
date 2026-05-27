import logging
import bcrypt
from sqlalchemy.ext.asyncio import AsyncSession
from secom.app.models.user_model import UserModel
from secom.app.repositories.user_repository import UserRepository
from secom.app.schemas.user_schema import UserSchema, LoginSchema

logger = logging.getLogger(__name__)


def _hash_password(plain: str) -> str:
    return bcrypt.hashpw(plain.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def _verify_password(plain: str, stored: str) -> bool:
    if not stored:
        return False
    try:
        return bcrypt.checkpw(plain.encode("utf-8"), stored.encode("utf-8"))
    except (ValueError, TypeError):
        return False


class UserService:

    def __init__(self) -> None:
        self.user_repository = UserRepository()

    async def save_user(self, session: AsyncSession, user_schema: UserSchema) -> UserModel:
        hashed = user_schema.model_copy(update={"password": _hash_password(user_schema.password)})
        user = await self.user_repository.save_user(session, hashed)
        logger.info("[UserService] save_user 레이어 완료 — userId=%s", user.user_id)
        return user

    async def login_user(self, session: AsyncSession, login_schema: LoginSchema) -> UserModel | None:
        user = await self.user_repository.find_by_email(session, login_schema.email)
        if user is None:
            logger.info("[UserService] login_user 실패 — 미가입 email=%s", login_schema.email)
            return None

        if _verify_password(login_schema.password, user.password):
            logger.info("[UserService] login_user 성공(해시) — email=%s", login_schema.email)
            return user

        if user.password == login_schema.password:
            user.password = _hash_password(login_schema.password)
            await session.commit()
            logger.info("[UserService] login_user 성공(평문→해시 마이그레이션) — email=%s", login_schema.email)
            return user

        logger.info("[UserService] login_user 실패 — 비번 불일치 email=%s", login_schema.email)
        return None
