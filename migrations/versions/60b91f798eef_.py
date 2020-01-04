"""empty message

Revision ID: 60b91f798eef
Revises: fdb9853cc72a
Create Date: 2020-01-04 15:01:46.502692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60b91f798eef'
down_revision = 'fdb9853cc72a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###