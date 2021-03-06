"""empty message

Revision ID: f97bb79d7197
Revises: 
Create Date: 2019-08-28 12:30:27.387205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f97bb79d7197'
down_revision = None
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
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('href')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job_article')
    # ### end Alembic commands ###
