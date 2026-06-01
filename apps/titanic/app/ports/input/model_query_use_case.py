from abc import ABC, abstractmethod


class ModelQueryUseCasePort(ABC):

    @abstractmethod
    def get_model_name(self) -> str: ...

    @abstractmethod
    def get_accuracy(self) -> float: ...

    @abstractmethod
    def get_tree(self) -> str: ...
