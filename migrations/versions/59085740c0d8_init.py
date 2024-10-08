"""init

Revision ID: 59085740c0d8
Revises: 
Create Date: 2024-08-19 17:06:41.621546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '59085740c0d8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cves',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cve_id', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('problem_types', sa.String(), nullable=True),
    sa.Column('published_date', sa.DateTime(), nullable=False),
    sa.Column('last_modified_date', sa.DateTime(), nullable=False),
    sa.Column('raw_info', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cve_id')
    )
    op.create_index(op.f('ix_cves_id'), 'cves', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cves_id'), table_name='cves')
    op.drop_table('cves')
    # ### end Alembic commands ###
