"""Added rules to models.

Revision ID: 4d94c06d5342
Revises: 1acac3085b66
Create Date: 2013-09-27 19:12:45.209762

"""

# revision identifiers, used by Alembic.
revision = '4d94c06d5342'
down_revision = '1acac3085b66'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bf_user', u'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('category', u'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('connection', u'access_token',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('connection', u'service',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('lesson', u'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('service', u'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('step', u'lesson_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user_to_lesson', u'lesson_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user_to_lesson', u'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_to_lesson', u'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('user_to_lesson', u'lesson_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('step', u'lesson_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('service', u'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('lesson', u'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('connection', u'service',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('connection', u'access_token',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('category', u'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('bf_user', u'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    ### end Alembic commands ###
