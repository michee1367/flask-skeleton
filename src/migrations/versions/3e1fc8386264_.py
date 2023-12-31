"""empty message

Revision ID: 3e1fc8386264
Revises: 92f315230f96
Create Date: 2023-06-29 20:22:54.445073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e1fc8386264'
down_revision = '92f315230f96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('provinces')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('provinces',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('population', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('area', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('income', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='provinces_pkey')
    )
    # ### end Alembic commands ###
