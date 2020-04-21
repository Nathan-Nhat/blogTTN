"""empty message

Revision ID: 8cb2985c16ff
Revises: c7f0ec1c20d8
Create Date: 2020-04-20 11:40:42.045635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cb2985c16ff'
down_revision = 'c7f0ec1c20d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###