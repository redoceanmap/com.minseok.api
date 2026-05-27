from typing import Optional

from pydantic import BaseModel, Field


class CaledonValidation(BaseModel):
    PassengerId: Optional[int] = Field(None, description="승객 ID")
    Survived: Optional[int] = Field(None, description="생존 여부 (0 = 사망, 1 = 생존)")
    Pclass: Optional[int] = Field(None, description="티켓 클래스 (1 = 1등석, 2 = 2등석, 3 = 3등석)")
    Name: Optional[str] = Field(None, description="이름")
    Sex: Optional[str] = Field(None, description="성별")
    Age: Optional[float] = Field(None, description="나이")
    SibSp: Optional[int] = Field(None, description="함께 탑승한 자녀 / 배우자 의 수")
    Parch: Optional[int] = Field(None, description="함께 탑승한 부모님 / 아이들 의 수")
    Ticket: Optional[str] = Field(None, description="티켓 번호")
    Fare: Optional[float] = Field(None, description="탑승 요금")
    Cabin: Optional[str] = Field(None, description="수하물 번호")
    Boat: Optional[str] = Field(None, description="탈출한 보트가 있다면 boat 번호")
    Embarked: Optional[str] = Field(None, description="선착장 (C = Cherbourg, Q = Queenstown, S = Southampton)")
