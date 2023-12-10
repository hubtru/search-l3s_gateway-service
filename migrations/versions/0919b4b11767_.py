"""empty message

Revision ID: 0919b4b11767
Revises: f9dbe40f3109
Create Date: 2023-10-23 21:43:56.296871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0919b4b11767'
down_revision = 'f9dbe40f3109'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Task', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Task', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)

    # ### end Alembic commands ###
