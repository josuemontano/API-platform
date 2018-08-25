"""Create posts table

Revision ID: 29a78f538297
Revises: 58564bb64da0
Create Date: 2018-08-25 12:12:35.181154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29a78f538297'
down_revision = '58564bb64da0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('title', sa.String(length=100), nullable=False),
                    sa.Column('body', sa.Text(), nullable=True),
                    sa.Column('is_published', sa.Boolean(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('deleted_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_posts'))
                    )


def downgrade():
    op.drop_table('posts')
