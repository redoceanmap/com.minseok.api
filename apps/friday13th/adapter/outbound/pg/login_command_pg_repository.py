import logging
from sqlalchemy import select
from backend.core.database import AsyncSessionLocal
from backend.apps.friday13th.domain.entities.user_entity import UserModel
from backend.apps.friday13th.app.ports.output.login_command_repository import LoginCommandRepositoryPort

logger = logging.getLogger(__name__)


class LoginCommandPgRepository(LoginCommandRepositoryPort):

    async def find_by_email(self, email: str) -> UserModel | None:
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(UserModel).where(UserModel.email == email))
            return result.scalars().first()

    async def update_password(self, email: str, new_password: str) -> None:
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(UserModel).where(UserModel.email == email))
            user = result.scalars().first()
            if user:
                user.password = new_password
                await session.commit()
                logger.info("[LoginCommandPgRepository] 비밀번호 마이그레이션 완료 — email=%s", email)
