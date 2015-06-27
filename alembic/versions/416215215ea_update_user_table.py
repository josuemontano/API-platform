"""Update user table

Revision ID: 416215215ea
Revises: 342f2b15873
Create Date: 2015-06-26 22:50:32.096796

"""

# revision identifiers, used by Alembic.
revision = '416215215ea'
down_revision = '342f2b15873'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('users', sa.Column('email', sa.String(length=250), nullable=False))
    op.create_unique_constraint(None, 'users', ['email'])
    op.drop_column('users', 'display_name')


def downgrade():
    op.add_column('users', sa.Column('display_name', sa.VARCHAR(length=150), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'email')
