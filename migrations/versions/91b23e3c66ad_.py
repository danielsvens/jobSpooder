"""empty message

Revision ID: 91b23e3c66ad
Revises: 86ca930f3e95
Create Date: 2019-08-25 15:13:07.605282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91b23e3c66ad'
down_revision = '86ca930f3e95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('step_stone', 'company',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('step_stone', 'href',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
    op.alter_column('step_stone', 'title',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('step_stone', 'title',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('step_stone', 'href',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
    op.alter_column('step_stone', 'company',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    # ### end Alembic commands ###
