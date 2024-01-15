"""casecade id dosen

Revision ID: 5033c45f5349
Revises: 6612f52a9ac9
Create Date: 2024-01-15 22:05:59.011024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5033c45f5349'
down_revision = '6612f52a9ac9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint('mahasiswa_ibfk_2', type_='foreignkey')
        batch_op.drop_constraint('mahasiswa_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_satu'], ['id'], ondelete='CASECADE')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_dua'], ['id'], ondelete='CASECADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('mahasiswa_ibfk_1', 'dosen', ['dosen_dua'], ['id'])
        batch_op.create_foreign_key('mahasiswa_ibfk_2', 'dosen', ['dosen_satu'], ['id'])

    # ### end Alembic commands ###
