"""empty message

Revision ID: bdc34ec849c5
Revises: 714f008975c9
Create Date: 2023-06-29 20:13:39.929403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdc34ec849c5'
down_revision = '714f008975c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inserttable', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=80), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inserttable', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
