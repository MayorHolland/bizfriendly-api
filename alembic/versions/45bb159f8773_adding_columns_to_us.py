"""Adding columns to user.

Revision ID: 45bb159f8773
Revises: 558fcfd1fb
Create Date: 2013-10-04 14:10:44.700332

"""

# revision identifiers, used by Alembic.
revision = '45bb159f8773'
down_revision = '558fcfd1fb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bf_user', sa.Column('business_name', sa.Unicode(), nullable=True))
    op.add_column('bf_user', sa.Column('location', sa.Unicode(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bf_user', 'location')
    op.drop_column('bf_user', 'business_name')
    ### end Alembic commands ###
