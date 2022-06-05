"""empty message

Revision ID: 2eaa6babbfdf
Revises: bc83de885d26
Create Date: 2022-05-28 03:31:01.547246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2eaa6babbfdf'
down_revision = 'bc83de885d26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recycle_item', sa.Column('item_category', sa.Text(), server_default='1', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recycle_item', 'item_category')
    # ### end Alembic commands ###