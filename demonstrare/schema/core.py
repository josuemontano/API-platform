from marshmallow import Schema, fields


class PostSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    body = fields.String()
    is_published = fields.Boolean()
    created = fields.DateTime()
    edited = fields.DateTime()
