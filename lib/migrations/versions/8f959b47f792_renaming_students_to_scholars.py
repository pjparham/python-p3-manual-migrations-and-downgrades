"""Renaming students to scholars

Revision ID: 8f959b47f792
Revises: 791279dd0760
Create Date: 2023-04-10 15:38:13.430311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f959b47f792'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
