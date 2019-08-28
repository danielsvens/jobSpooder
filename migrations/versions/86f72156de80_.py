"""empty message

Revision ID: 86f72156de80
Revises: 6117dae4d197
Create Date: 2019-08-28 12:53:36.891969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86f72156de80'
down_revision = '6117dae4d197'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job_article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('site', sa.String(length=80), nullable=True),
    sa.Column('href', sa.String(length=250), nullable=True),
    sa.Column('title', sa.String(length=250), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('company', sa.String(length=80), nullable=True),
    sa.Column('image', sa.String(length=250), nullable=True),
    sa.Column('city', sa.String(length=80), nullable=True),
    sa.Column('days_left', sa.String(length=80), nullable=True),
    sa.Column('created', sa.String(length=80), nullable=True),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job_article')
    # ### end Alembic commands ###