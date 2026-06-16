from pydantic import BaseModel, Field

'''
캐릭터: 몰리 후퍼 (Molly)
역할 (keyword): examiner (검증/조사관)
드라마 설정 및 시스템 기능: 세인트 바톨로뮤 병원의 부검의. 시스템에 유입되는 데이터의 유효성 검증(Validation) 및 팩트 체크를 수행합니다.
'''

class MollyExaminerSchema(BaseModel):

    id: int = Field(0, description="몰리 후퍼 (Molly) ID")
    name: str = Field("몰리 후퍼 (Molly)", description="검증/조사관")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 4,
                "name": "Molly examiner",
            }
        }
    }
