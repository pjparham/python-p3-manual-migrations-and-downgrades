"""Renaming grade column in Students to year

Revision ID: 804f40db6fb7
Revises: 8f959b47f792
Create Date: 2023-04-10 16:32:37.528155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '804f40db6fb7'
down_revision = '8f959b47f792'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'grade', new_column_name='year')


def downgrade() -> None:
    pass
