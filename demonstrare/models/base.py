from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr, declarative_base

Base = declarative_base()


class ModelMixin(object):
    @declared_attr
    def created(self):
        return Column(DateTime, nullable=False, default=datetime.utcnow)
    
    @declared_attr
    def edited(self):
        return Column(DateTime, onupdate=datetime.utcnow)
