from abc import ABC, abstractmethod
from backend.apps.friday13th.domain.entities.user_entity import UserModel


class LoginCommandRepositoryPort(ABC):

    @abstractmethod
    async def find_by_email(self, email: str) -> UserModel | None: ...

    @abstractmethod
    async def update_password(self, email: str, new_password: str) -> None: ...
