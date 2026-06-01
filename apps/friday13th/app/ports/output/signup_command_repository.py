from abc import ABC, abstractmethod
from backend.apps.friday13th.domain.entities.user_entity import UserModel
from backend.apps.friday13th.adapter.inbound.api.schemas.user_schema import UserSchema


class SignupCommandRepositoryPort(ABC):

    @abstractmethod
    async def save_user(self, user_schema: UserSchema) -> UserModel: ...
