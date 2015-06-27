from sqlalchemy import Boolean, Column, Integer, String, Text

from .base import Base, ModelMixin


class Post(Base, ModelMixin):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    body = Column(Text)
    is_published = Column(Boolean, nullable=False, default=True)
