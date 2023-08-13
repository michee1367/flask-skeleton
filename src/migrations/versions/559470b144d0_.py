"""empty message

Revision ID: 559470b144d0
Revises: d5546922238e
Create Date: 2023-08-12 12:08:48.978956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '559470b144d0'
down_revision = 'd5546922238e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.drop_table('spatial_ref_sys')
    with op.batch_alter_table('existing_plant_existing_plant', schema=None) as batch_op:
        batch_op.drop_index('idx_existing_plant_existing_plant_geom_0')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('existing_plant_existing_plant', schema=None) as batch_op:
        batch_op.create_index('idx_existing_plant_existing_plant_geom_0', ['geom'], unique=False)

    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('srid > 0 AND srid <= 998999', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    # ### end Alembic commands ###