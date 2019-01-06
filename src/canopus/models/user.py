from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_utils import ChoiceType, EmailType, PhoneNumberType

from .base import BaseModel
from .lib import OrderedEnum
from .meta import Base


class Role(OrderedEnum):
    USER = 10
    ADMIN = 20


class User(Base, BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(EmailType)
    phone = Column(PhoneNumberType())
    role = Column(ChoiceType(Role, impl=Integer()), nullable=False)
    is_enabled = Column(Boolean, nullable=False, default=True)

    last_signed_in_at = Column(DateTime)

    @hybrid_property
    def is_admin(self):
        role = self.role
        return role and role >= Role.ADMIN

    @hybrid_property
    def name(self):
        return f'{self.first_name} {self.last_name}'
