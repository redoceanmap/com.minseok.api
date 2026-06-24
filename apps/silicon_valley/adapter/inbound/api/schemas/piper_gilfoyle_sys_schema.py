from pydantic import BaseModel, Field

class GilfoyleSysSchema(BaseModel):

    id: int = Field(0, description="Pied Piper ID")
    name: str = Field("버트람 길포일", description="Member's name")
    # 시스템·네트워크 아키텍트. 인프라와 서버를 책임지는 냉소적인 시스템 엔지니어

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 2,
                "name": "Bertram Gilfoyle",
            }
        }
    }
