from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr


class ModelMixin(object):
    @declared_attr
    def created(self):
        return Column(DateTime, nullable=False, default=datetime.now)

    @declared_attr
    def edited(self):
        return Column(DateTime, onupdate=datetime.now)

    @declared_attr
    def deleted(self):
        return Column(DateTime)
