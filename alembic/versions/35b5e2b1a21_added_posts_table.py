"""Added posts table

Revision ID: 35b5e2b1a21
Revises: 
Create Date: 2015-04-27 12:51:46.518794

"""

# revision identifiers, used by Alembic.
revision = '35b5e2b1a21'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(length=100), nullable=False),
                    sa.Column('body', sa.Text(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('is_published', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('posts')
