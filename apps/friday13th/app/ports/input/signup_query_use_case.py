from abc import ABC, abstractmethod


class SignupQueryUseCasePort(ABC):

    @abstractmethod
    async def is_email_available(self, email: str) -> bool: ...
