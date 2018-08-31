from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utils import generic_repr


@generic_repr
class BaseModel:
    @declared_attr
    def created_at(self):
        return Column(DateTime, nullable=False, default=datetime.utcnow)

    @declared_attr
    def updated_at(self):
        return Column(DateTime, onupdate=datetime.utcnow)

    @declared_attr
    def deleted_at(self):
        return Column(DateTime)
