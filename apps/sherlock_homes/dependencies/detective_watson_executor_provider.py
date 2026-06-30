from fastapi import Depends

from sherlock_homes.adapter.outbound.n8n.detective_watson_executor_n8n_adapter import WatsonExecutorN8nAdapter
from sherlock_homes.app.ports.input.detective_watson_executor_use_case import WatsonExecutorUseCase
from sherlock_homes.app.ports.output.detective_watson_executor_port import WatsonExecutorPort
from sherlock_homes.app.use_cases.detective_watson_executor_interactor import WatsonExecutorInteractor


def get_watson_executor_repository() -> WatsonExecutorPort:
    return WatsonExecutorN8nAdapter()


def get_watson_executor_use_case(
        repository: WatsonExecutorPort = Depends(get_watson_executor_repository)
) -> WatsonExecutorUseCase:
    return WatsonExecutorInteractor(port=repository)
