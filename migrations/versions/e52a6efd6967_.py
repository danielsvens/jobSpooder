"""empty message

Revision ID: e52a6efd6967
Revises: 199bcf261491
Create Date: 2019-08-25 13:23:00.237765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e52a6efd6967'
down_revision = '199bcf261491'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('step_stone', 'days_left',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=80),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('step_stone', 'days_left',
               existing_type=sa.String(length=80),
               type_=sa.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###
