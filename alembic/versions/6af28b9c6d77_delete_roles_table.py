"""Delete roles table

Revision ID: 6af28b9c6d77
Revises: 31cec720de8
Create Date: 2016-10-25 23:53:00.811791

"""

# revision identifiers, used by Alembic.
revision = '6af28b9c6d77'
down_revision = '31cec720de8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('users', sa.Column('role', sa.Integer(), nullable=False))
    op.drop_constraint('users_role_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    op.drop_table('roles')


def downgrade():
    op.drop_column('users', 'role')
    op.create_table('roles',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
                    sa.Column('is_default', sa.BOOLEAN(), autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='roles_pkey')
                    )
    op.add_column('users', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('users_role_id_fkey', 'users', 'roles', ['role_id'], ['id'])
