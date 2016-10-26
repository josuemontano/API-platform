from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr


class ModelMixin(object):
    @declared_attr
    def created_at(self):
        return Column(DateTime, nullable=False, default=datetime.now)

    @declared_attr
    def updated_at(self):
        return Column(DateTime, onupdate=datetime.now)

    @declared_attr
    def deleted_at(self):
        return Column(DateTime)
