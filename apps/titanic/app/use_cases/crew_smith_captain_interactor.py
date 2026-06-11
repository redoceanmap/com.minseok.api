from __future__ import annotations

from fastapi import Depends

from titanic.adapter.inbound.api.schemas.crew_smith_captain_schema import ChatSchema, SmithCaptainSchema
from titanic.app.dtos.crew_smith_captain_dto import SmithCaptainQuery, SmithCaptainResponse, SmithChatQuery, SmithChatResponse
from titanic.app.ports.input.crew_smith_captain_use_case import SmithCaptainUseCase
from titanic.app.ports.input.passenger_jack_trainer_use_case import JackTrainerUseCase
from titanic.app.ports.input.passenger_rose_model_use_case import RoseModelUseCase
from titanic.app.ports.output.crew_smith_captain_repository import SmithCaptainRepository
from titanic.dependencies.passenger_jack_trainer_provider import get_jack_trainer
from titanic.dependencies.passenger_rose_model_provider import get_rose_model


class SmithCaptainInteractor(SmithCaptainUseCase):

    def __init__(self, repository: SmithCaptainRepository):
        self.repository = repository
        
    async def chat(self, schema: ChatSchema,
        jack: JackTrainerUseCase = Depends(get_jack_trainer), 
        rose: RoseModelUseCase = Depends(get_rose_model)
        ) -> SmithChatResponse:
        
        '''사용자의 자연어 입력을 처리하는 채팅 인터렉트'''

        return await self.repository.chat(SmithChatQuery(
            message = schema.message
        ))
        
        
    async def introduce_myself(self, schema: SmithCaptainSchema) -> SmithCaptainResponse:
        '''스미스 선장의 자기소개 인터렉트'''

        return await self.repository.introduce_myself(SmithCaptainQuery(
            id = schema.id,
            name = schema.name
        ))


