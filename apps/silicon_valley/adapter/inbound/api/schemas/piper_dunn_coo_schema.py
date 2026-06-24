from pydantic import BaseModel, Field

class DunnCooSchema(BaseModel):

    id: int = Field(0, description="Pied Piper ID")
    name: str = Field("도널드 '자레드' 던", description="Member's name")
    # 파이드 파이퍼의 COO. 회사의 운영과 살림을 도맡는 헌신적인 비즈니스 책임자

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 4,
                "name": "Donald 'Jared' Dunn",
            }
        }
    }
