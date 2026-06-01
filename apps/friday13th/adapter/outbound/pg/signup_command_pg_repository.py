import logging
from backend.core.database import AsyncSessionLocal
from backend.apps.friday13th.domain.entities.user_entity import UserModel
from backend.apps.friday13th.adapter.inbound.api.schemas.user_schema import UserSchema
from backend.apps.friday13th.app.ports.output.signup_command_repository import SignupCommandRepositoryPort

logger = logging.getLogger(__name__)


class SignupCommandPgRepository(SignupCommandRepositoryPort):

    async def save_user(self, user_schema: UserSchema) -> UserModel:
        async with AsyncSessionLocal() as session:
            user = UserModel(
                user_id=user_schema.userId,
                password=user_schema.password,
                nickname=user_schema.nickname,
                email=user_schema.email,
                role=user_schema.role,
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
            logger.info("[SignupCommandPgRepository] save_user 완료 — userId=%s", user.user_id)
            return user
