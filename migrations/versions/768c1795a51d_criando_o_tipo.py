"""criando o tipo

Revision ID: 768c1795a51d
Revises: 6e9088c8f5c2
Create Date: 2024-05-14 20:00:05.141193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '768c1795a51d'
down_revision = '6e9088c8f5c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tipo')
    # ### end Alembic commands ###