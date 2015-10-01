"""Create role model

Revision ID: 1c90823a0fb
Revises: 416215215ea
Create Date: 2015-06-26 23:17:48.895175

"""

# revision identifiers, used by Alembic.
revision = '1c90823a0fb'
down_revision = '416215215ea'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('roles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('is_default', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.add_column('users', sa.Column('role_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])


def downgrade():
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    op.drop_table('roles')
