"""empty message

Revision ID: 7ec032bc2c72
Revises: 7a96aea4870b
Create Date: 2023-10-18 14:22:15.067932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ec032bc2c72'
down_revision = '7a96aea4870b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_constraint('test_public_id_2_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.create_unique_constraint('test_public_id_2_key', ['public_id_2'])

    # ### end Alembic commands ###
