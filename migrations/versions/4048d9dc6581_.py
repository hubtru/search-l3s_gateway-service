"""empty message

Revision ID: 4048d9dc6581
Revises: a8b610cf686f
Create Date: 2023-10-18 15:04:45.581410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4048d9dc6581'
down_revision = 'a8b610cf686f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.add_column(sa.Column('public_id', sa.String(length=256), server_default='<function Test.<lambda> at 0x7f261a556160>', nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_column('public_id')

    # ### end Alembic commands ###
