from pydantic import BaseModel, Field

class DineshDashSchema(BaseModel):

    id: int = Field(0, description="Pied Piper ID")
    name: str = Field("디네시 추타이", description="Member's name")
    # 파이드 파이퍼의 개발자. 길포일과 끊임없이 경쟁하는 프론트엔드·대시보드 담당 엔지니어

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 3,
                "name": "Dinesh Chugtai",
            }
        }
    }
