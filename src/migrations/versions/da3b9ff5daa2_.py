"""empty message

Revision ID: da3b9ff5daa2
Revises: 90565eb6eb49
Create Date: 2023-08-13 11:31:18.579226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da3b9ff5daa2'
down_revision = '90565eb6eb49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.drop_table('spatial_ref_sys')
    with op.batch_alter_table('projects_project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('plannedPower', sa.Float(), nullable=True))
        batch_op.alter_column('plannedPowerForHouseholds',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
        batch_op.alter_column('plannedPowerForProductive',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
        batch_op.alter_column('nbrHouseholds',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects_project', schema=None) as batch_op:
        batch_op.alter_column('nbrHouseholds',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('plannedPowerForProductive',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
        batch_op.alter_column('plannedPowerForHouseholds',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
        batch_op.drop_column('plannedPower')

    """op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('srid > 0 AND srid <= 998999', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )"""
    # ### end Alembic commands ###
