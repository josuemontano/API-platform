from marshmallow import Schema, fields, post_load

from ..models import Post


class PostSchema(Schema):
    __model__ = Post

    id = fields.Integer()
    title = fields.String()
    body = fields.String()
    is_published = fields.Boolean()

    class Meta:
        ordered = True

    @post_load
    def make_object(self, data):
        return self.__model__(**data)
