from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import ModelMixin
from .meta import Base


class Role:
    USER = 10
    ADMIN = 20


class User(Base, ModelMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(250))
    phone = Column(String(50))
    role = Column(Integer, nullable=False)
    enabled = Column(Boolean, nullable=False, default=True)
    last_signed_in_at = Column(DateTime)
