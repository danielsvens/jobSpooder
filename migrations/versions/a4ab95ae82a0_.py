"""empty message

Revision ID: a4ab95ae82a0
Revises: 1c9ccf79e38e
Create Date: 2019-08-25 16:55:13.548756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4ab95ae82a0'
down_revision = '1c9ccf79e38e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('monster',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('href', sa.String(length=250), nullable=True),
    sa.Column('title', sa.String(length=250), nullable=True),
    sa.Column('company', sa.String(length=80), nullable=True),
    sa.Column('image', sa.String(length=250), nullable=True),
    sa.Column('city', sa.String(length=80), nullable=True),
    sa.Column('created', sa.String(length=80), nullable=True),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('monster')
    # ### end Alembic commands ###
