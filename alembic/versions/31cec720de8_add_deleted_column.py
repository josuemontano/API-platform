"""Add deleted column

Revision ID: 31cec720de8
Revises: 5a1c1848311
Create Date: 2015-10-01 15:09:57.225329

"""

# revision identifiers, used by Alembic.
revision = '31cec720de8'
down_revision = '5a1c1848311'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('posts', sa.Column('deleted', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('deleted', sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column('users', 'deleted')
    op.drop_column('posts', 'deleted')
