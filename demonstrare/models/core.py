from .base import Base, ModelMixin

from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class User(Base, ModelMixin):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    display_name = Column(String(150))
    facebook = Column(String(120))
    google = Column(String(120))
    twitter = Column(String(120))

    def __init__(self, display_name, facebook=None, google=None, twitter=None):
        self.display_name = display_name
        if facebook:
            self.facebook = facebook
        if google:
            self.google = google
        if twitter:
            self.twitter = twitter


class Post(Base, ModelMixin):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    body = Column(Text)
    is_published = Column(Boolean, nullable=False, default=True)

    @classmethod
    def serializer(cls):
        return {
            'id': 'id',
            'title': 'title',
            'created': 'created',
        }
