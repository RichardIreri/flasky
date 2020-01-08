"""empty message

Revision ID: 981d6d057e9d
Revises: 341ed0e1a324
Create Date: 2020-01-08 14:34:11.935578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '981d6d057e9d'
down_revision = '341ed0e1a324'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###
