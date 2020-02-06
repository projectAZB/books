"""base

Revision ID: aa35f4e80738
Revises: 
Create Date: 2020-02-06 19:00:12.328750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa35f4e80738'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(250), nullable=False, index=True),
        sa.Column('author', sa.String(250), nullable=False),
        sa.Column('genre', sa.String(250))
    )


def downgrade():
    op.drop_table('books')
