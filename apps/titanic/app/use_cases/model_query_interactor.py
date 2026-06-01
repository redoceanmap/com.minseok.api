import logging
from backend.apps.titanic.app.ports.input.model_query_use_case import ModelQueryUseCasePort
from backend.apps.titanic.app.ports.output.model_query_repository import ModelQueryRepositoryPort

logger = logging.getLogger(__name__)


class ModelQueryInteractor(ModelQueryUseCasePort):

    def __init__(self, model_repository: ModelQueryRepositoryPort) -> None:
        self._model_repository = model_repository

    def get_model_name(self) -> str:
        return self._model_repository.get_model_name()

    def get_accuracy(self) -> float:
        return self._model_repository.get_accuracy()

    def get_tree(self) -> str:
        return self._model_repository.get_tree()
