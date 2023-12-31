"""empty message

Revision ID: 9714c979e051
Revises: 
Create Date: 2023-06-09 16:22:58.946024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9714c979e051'
down_revision = None
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
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inserttable')
    # ### end Alembic commands ###
