"""followers

Revision ID: 13c3a45940c2
Revises: 621cea6ee525
Create Date: 2020-07-06 12:11:29.855611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13c3a45940c2'
down_revision = '621cea6ee525'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
