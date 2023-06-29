"""empty message

Revision ID: f0b777c1d742
Revises: 2eec90bf56b4
Create Date: 2023-06-29 20:25:48.109144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0b777c1d742'
down_revision = '2eec90bf56b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inserttable',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('machineid', sa.Integer(), nullable=True),
    sa.Column('stateid', sa.Integer(), nullable=True),
    sa.Column('speed', sa.Integer(), nullable=False),
    sa.Column('statechange', sa.Integer(), nullable=False),
    sa.Column('unixtime', sa.Integer(), nullable=False),
    sa.Column('extras', sa.String(length=80), nullable=False),
    sa.Column('state', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inserttable')
    # ### end Alembic commands ###
