from marshmallow import Schema, fields, post_load

from ..models import User


class UserSchema(Schema):
    __model__ = User

    id = fields.Integer()
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(allow_none=True)
    phone = fields.String(allow_none=True)
    role = fields.Integer(required=True)
    enabled = fields.Boolean()

    class Meta:
        ordered = True

    @post_load
    def make_object(self, data):
        return self.__model__(**data)
