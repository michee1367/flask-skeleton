"""empty message

Revision ID: d5546922238e
Revises: 275382cd42e0
Create Date: 2023-08-12 11:47:55.050601

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision = 'd5546922238e'
down_revision = '275382cd42e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('existing_plant_existing_plant',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('power', sa.Float(), nullable=False),
    sa.Column('nbrOfhouseholds', sa.Integer(), nullable=False),
    sa.Column('powerForProductiveUsed', sa.Float(), nullable=False),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POINT', srid=4326, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('existing_plant_existing_plant', schema=None) as batch_op:
        batch_op.create_index('idx_existing_plant_existing_plant_geom_0', ['geom'], unique=False, postgresql_using='gist')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('existing_plant_existing_plant', schema=None) as batch_op:
        batch_op.drop_index('idx_existing_plant_existing_plant_geom', postgresql_using='gist')

    op.drop_table('existing_plant_existing_plant')
    # ### end Alembic commands ###