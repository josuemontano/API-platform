"""Add created and edited columns to tables

Revision ID: 342f2b15873
Revises: 32e02371174
Create Date: 2015-05-11 19:48:42.520385

"""

# revision identifiers, used by Alembic.
revision = '342f2b15873'
down_revision = '32e02371174'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('users', sa.Column('created', sa.DateTime(), nullable=False))
    op.add_column('users', sa.Column('edited', sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column('users', 'edited')
    op.drop_column('users', 'created')
