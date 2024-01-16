"""edit user tabel

Revision ID: 89747849cd6e
Revises: 5033c45f5349
Create Date: 2024-01-16 17:33:06.936388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89747849cd6e'
down_revision = '5033c45f5349'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'dosen', ['dosen_satu'], ['id'], ondelete='NOT NULL')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_dua'], ['id'], ondelete='NOT NULL')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('level', sa.BigInteger(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('level')

    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
