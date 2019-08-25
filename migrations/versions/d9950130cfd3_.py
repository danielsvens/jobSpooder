"""empty message

Revision ID: d9950130cfd3
Revises: 71946ba532bf
Create Date: 2019-08-25 12:42:19.524478

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd9950130cfd3'
down_revision = '71946ba532bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('step_stone', 'created',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.String(length=80),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('step_stone', 'created',
               existing_type=sa.String(length=80),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    # ### end Alembic commands ###