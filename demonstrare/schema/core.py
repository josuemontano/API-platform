from marshmallow import Schema, fields

from ..models.core import Post


class PostSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    body = fields.String()
    is_published = fields.Boolean()

    def make_object(self, data):
        return Post(**data)
