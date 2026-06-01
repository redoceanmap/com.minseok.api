from abc import ABC, abstractmethod
from backend.apps.friday13th.domain.entities.user_entity import UserModel
from backend.apps.friday13th.adapter.inbound.api.schemas.user_schema import LoginSchema


class LoginCommandUseCasePort(ABC):

    @abstractmethod
    async def login_user(self, login_schema: LoginSchema) -> UserModel | None: ...
