from marshmallow_enum import EnumField
from marshmallow_sqlalchemy import ModelSchema

from ..models import Role, User


class UserSchema(ModelSchema):
    class Meta:
        model = User
        dump_only = ('created_at', 'last_signed_in_at', 'updated_at')
        exclude = ('deleted_at',)

    role = EnumField(Role, by_value=True, required=True)
