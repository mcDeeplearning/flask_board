"""empty message

Revision ID: b2ec8ae24671
Revises: 6a96a96e7f45
Create Date: 2018-11-09 02:23:49.290990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2ec8ae24671'
down_revision = '6a96a96e7f45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('creator', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'creator')
    # ### end Alembic commands ###
