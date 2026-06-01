from abc import ABC, abstractmethod
from backend.apps.friday13th.domain.entities.user_entity import UserModel


class SignupQueryRepositoryPort(ABC):

    @abstractmethod
    async def find_by_email(self, email: str) -> UserModel | None: ...
