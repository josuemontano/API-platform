"""Add columns to users table

Revision ID: a475059c6315
Revises: 6af28b9c6d77
Create Date: 2016-10-25 23:59:39.247272

"""

# revision identifiers, used by Alembic.
revision = 'a475059c6315'
down_revision = '6af28b9c6d77'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_column('users', 'google')
    op.drop_column('users', 'live')
    op.drop_column('users', 'facebook')

    op.add_column('users', sa.Column('enabled', sa.Boolean(), nullable=False, server_default='t'))
    op.add_column('users', sa.Column('first_name', sa.String(length=100), nullable=False))
    op.add_column('users', sa.Column('last_name', sa.String(length=100), nullable=False))
    op.add_column('users', sa.Column('last_signed_in_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('phone', sa.String(length=50), nullable=True))
    op.alter_column('users', 'email', existing_type=sa.VARCHAR(length=250), nullable=True)


def downgrade():
    op.add_column('users', sa.Column('facebook', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('live', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('google', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.alter_column('users', 'email', existing_type=sa.VARCHAR(length=250), nullable=False)
    op.create_unique_constraint('users_email_key', 'users', ['email'])

    op.drop_column('users', 'phone')
    op.drop_column('users', 'last_signed_in_at')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'enabled')
