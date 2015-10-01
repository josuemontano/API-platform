"""Replace twitter column with live

Revision ID: 5a1c1848311
Revises: 1c90823a0fb
Create Date: 2015-10-01 14:02:06.755139

"""

# revision identifiers, used by Alembic.
revision = '5a1c1848311'
down_revision = '1c90823a0fb'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('users', sa.Column('live', sa.String(length=120), nullable=True))
    op.drop_column('users', 'twitter')


def downgrade():
    op.add_column('users', sa.Column('twitter', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('users', 'live')
