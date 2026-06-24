from pydantic import BaseModel, Field

class HendricksCeoSchema(BaseModel):

    id: int = Field(0, description="Pied Piper ID")
    name: str = Field("리처드 헨드릭스", description="Member's name")
    # 파이드 파이퍼의 창업자이자 CEO. 미들아웃 압축 알고리즘을 만든 천재 개발자

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "name": "Richard Hendricks",
            }
        }
    }
