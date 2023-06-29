"""empty message

Revision ID: cd1a7fbb0b1e
Revises: 3b4dc1df86c3
Create Date: 2023-06-29 20:50:43.530472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd1a7fbb0b1e'
down_revision = '3b4dc1df86c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('area', sa.Float(), nullable=False),
    sa.Column('income', sa.Float(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('city')
    # ### end Alembic commands ###