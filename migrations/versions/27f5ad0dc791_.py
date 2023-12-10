"""empty message

Revision ID: 27f5ad0dc791
Revises: 57f89b1ac4aa
Create Date: 2023-10-19 09:40:44.129328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27f5ad0dc791'
down_revision = '57f89b1ac4aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_column('another_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.add_column(sa.Column('another_id', sa.VARCHAR(length=256), server_default=sa.text("lower('536a3f13-590b-4eee-9b69-40670a6b5461'::text)"), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
