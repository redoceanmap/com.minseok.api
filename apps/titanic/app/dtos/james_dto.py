from typing import Any

from pydantic import BaseModel


class JamesUploadDto(BaseModel):
    count: int
    data: list[dict[str, Any]]
