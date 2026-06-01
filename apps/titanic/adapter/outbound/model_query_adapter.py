from backend.apps.titanic.app.ports.output.model_query_repository import ModelQueryRepositoryPort
from backend.apps.titanic.app.use_cases.train_interactor import JackService


class ModelQueryAdapter(ModelQueryRepositoryPort):

    def __init__(self, jack: JackService) -> None:
        self._jack = jack

    def get_model_name(self) -> str:
        return self._jack.get_model()

    def get_accuracy(self) -> float:
        return self._jack.get_accuracy()

    def get_tree(self) -> str:
        return self._jack.get_tree()
