from sqlalchemy import Column, Integer, String
from backend.core.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    password = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role = Column(String, nullable=False, default="user")
