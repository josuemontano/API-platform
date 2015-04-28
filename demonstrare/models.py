from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(150))
    display_name = Column(String(150))
    facebook = Column(String(120))
    google = Column(String(120))
    twitter = Column(String(120))

    def __init__(self, email=None, facebook=None, google=None, twitter=None):
        if email:
            self.email = email.lower()
        if facebook:
            self.facebook = facebook
        if google:
            self.google = google
        if twitter:
            self.twitter = twitter


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    body = Column(Text)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    edited = Column(DateTime, default=datetime.utcnow)
    is_published = Column(Boolean, nullable=False, default=True)

    @classmethod
    def serializer(cls):
        return {
            'id': 'id',
            'title': 'title',
            'created': 'created',
        }
