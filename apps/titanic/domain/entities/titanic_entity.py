from typing import Optional
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from backend.core.database import Base


class TitanicPassenger(Base):
    __tablename__ = "titanic_passengers"

    id: Mapped[int] = mapped_column(primary_key=True)
    passenger_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    survived: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    pclass: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    sex: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    age: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    sib_sp: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    parch: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    ticket: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    fare: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    cabin: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    boat: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    embarked: Mapped[Optional[str]] = mapped_column(String, nullable=True)
