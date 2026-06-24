from pydantic import BaseModel, Field

class BighettiHrSchema(BaseModel):

    id: int = Field(0, description="Pied Piper ID")
    name: str = Field("넬슨 '빅헤드' 비게티", description="Member's name")
    # 리처드의 오랜 친구. 얼떨결에 승진을 거듭하는 인사(HR) 담당 캐릭터

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 5,
                "name": "Nelson 'Big Head' Bighetti",
            }
        }
    }
