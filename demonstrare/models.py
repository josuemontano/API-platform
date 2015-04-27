from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    body = Column(Text)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    edited = Column(DateTime, default=datetime.utcnow)
    is_published = Column(Boolean, nullable=False, default=True)
