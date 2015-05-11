"""Added users table

Revision ID: 2aa08442e7b
Revises: 35b5e2b1a21
Create Date: 2015-04-27 20:28:26.013609

"""

# revision identifiers, used by Alembic.
revision = '2aa08442e7b'
down_revision = '35b5e2b1a21'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=150), nullable=False),
        sa.Column('password', sa.String(length=150), nullable=True),
        sa.Column('display_name', sa.String(length=150), nullable=True),
        sa.Column('facebook', sa.String(length=120), nullable=True),
        sa.Column('google', sa.String(length=120), nullable=True),
        sa.Column('twitter', sa.String(length=120), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )


def downgrade():
    op.drop_table('users')
