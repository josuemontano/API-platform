from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import ModelMixin
from .meta import Base


class Role:
    USER = 10
    ADMIN = 20


class User(Base, ModelMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False, unique=True)
    facebook = Column(String(120))
    google = Column(String(120))
    live = Column(String(120))
    role = Column(Integer, nullable=False)

    def __init__(self, email, role, facebook=None, google=None, live=None):
        self.email = email
        self.role = role
        self.role_id = role.id

        if facebook:
            self.facebook = facebook
        if google:
            self.google = google
        if live:
            self.live = live
