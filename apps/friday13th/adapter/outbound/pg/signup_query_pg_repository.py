import logging
from sqlalchemy import select
from backend.core.database import AsyncSessionLocal
from backend.apps.friday13th.domain.entities.user_entity import UserModel
from backend.apps.friday13th.app.ports.output.signup_query_repository import SignupQueryRepositoryPort

logger = logging.getLogger(__name__)


class SignupQueryPgRepository(SignupQueryRepositoryPort):

    async def find_by_email(self, email: str) -> UserModel | None:
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(UserModel).where(UserModel.email == email))
            return result.scalars().first()
