import logging

from kiwipiepy import Kiwi

from titanic.adapter.inbound.api.schemas.passenger_jack_trainer_schema import JackTrainerSchema
from titanic.app.dtos.passenger_jack_trainer_dto import JackTrainerQuery, JackTrainerResponse
from titanic.app.ports.input.passenger_jack_trainer_use_case import JackTrainerUseCase
from titanic.app.ports.output.passenger_jack_trainer_repository import JackTrainerRepository

logger = logging.getLogger(__name__)


class JackTrainerInteractor(JackTrainerUseCase):

    def __init__(self, repository: JackTrainerRepository):
        self.repository = repository
        self.kiwi = Kiwi()

    async def analyze_message_intent(self, user_message: str) -> dict:
        '''사용자의 질문(message)을 형태소 분석하여 키워드와 의도를 파악한다'''

        logger.info(f"[JackTrainerInteractor] 전처리 및 분석 시작 | message: {user_message}")

        tokens = self.kiwi.tokenize(user_message)

        keywords = []
        has_quantity_modifier = False
        has_count_unit = False

        for t in tokens:
            if t.tag in ('NNG', 'NNP'):
                keywords.append(t.form)

            if t.tag == 'MM' and t.form == '몇':
                has_quantity_modifier = True

            if t.tag == 'NNB' and t.form in ('명', '개', '사람', '분'):
                has_count_unit = True

        is_count_query = has_quantity_modifier or has_count_unit or ("몇" in user_message)

        intent = "question" if user_message.rstrip().endswith("?") else "statement"

        analysis_result = {
            "keywords": keywords,
            "is_count_query": is_count_query,
            "intent": intent
        }

        logger.info(f"[JackTrainerInteractor] 분석 완료 | 결과: {analysis_result}")
        return analysis_result

    async def introduce_myself(self, schema: JackTrainerSchema) -> JackTrainerResponse:
        '''잭 트레이너의 자기소개 인터렉트'''

        return await self.repository.introduce_myself(JackTrainerQuery(
            id = schema.id,
            name = schema.name
        ))
