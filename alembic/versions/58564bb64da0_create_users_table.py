"""Create users table

Revision ID: 58564bb64da0
Revises: 
Create Date: 2018-08-25 12:09:38.588448

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '58564bb64da0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('first_name', sa.String(length=100), nullable=False),
                    sa.Column('last_name', sa.String(length=100), nullable=False),
                    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=True),
                    sa.Column('phone', sqlalchemy_utils.types.phone_number.PhoneNumberType(length=20), nullable=True),
                    sa.Column('role', sa.Integer(), nullable=False),
                    sa.Column('is_enabled', sa.Boolean(), nullable=False, server_default='TRUE'),
                    sa.Column('last_signed_in_at', sa.DateTime(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('deleted_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
                    )


def downgrade():
    op.drop_table('users')
