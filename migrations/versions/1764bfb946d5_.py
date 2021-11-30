"""empty message

Revision ID: 1764bfb946d5
Revises: 77bc316d2b88
Create Date: 2017-09-07 17:43:59.798509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1764bfb946d5'
down_revision = '77bc316d2b88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
