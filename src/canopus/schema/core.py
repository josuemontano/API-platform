from marshmallow_sqlalchemy import ModelSchema

from ..models import Post


class PostSchema(ModelSchema):
    class Meta:
        model = Post
        dump_only = ('created_at', 'updated_at')
        exclude = ('deleted_at',)
