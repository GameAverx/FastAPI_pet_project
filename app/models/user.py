from datetime import datetime
from sqlalchemy.testing.schema import mapped_column
from pydantic import EmailStr
from app.core.database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy import DateTime,Column, String, Integer
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name =  Column(String(20), unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())






