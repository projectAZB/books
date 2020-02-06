"""base

Revision ID: cdfdfbe5fc22
Revises: 
Create Date: 2020-02-06 20:36:33.881866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdfdfbe5fc22'
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
    op.create_unique_constraint('_title_author_uc', 'books', ['author', 'title'], schema='books')


def downgrade():
    op.drop_table('books')
