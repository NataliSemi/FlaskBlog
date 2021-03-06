"""add language to posts

Revision ID: 63a6a8724dae
Revises: 842b24e4ff43
Create Date: 2021-02-25 21:53:16.355943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63a6a8724dae'
down_revision = '842b24e4ff43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
