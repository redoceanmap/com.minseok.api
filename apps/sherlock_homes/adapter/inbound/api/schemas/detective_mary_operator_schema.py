from pydantic import BaseModel, Field

'''
캐릭터: 메리 왓슨 (Mary)
역할 (keyword): operator (특수 작전/보안)
드라마 설정 및 시스템 기능: 사설 탐정단에 합류한 전직 비밀 요원. 시스템 내부의 예외 처리(Exception), 보안 우회 로직 및 긴급 특수 작전 코드를 수행합니다.
'''

class MaryOperatorSchema(BaseModel):

    id: int = Field(0, description="메리 왓슨 (Mary) ID")
    name: str = Field("메리 왓슨 (Mary)", description="특수 작전/보안")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 12,
                "name": "Mary operator",
            }
        }
    }
