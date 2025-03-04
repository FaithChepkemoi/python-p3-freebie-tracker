"""create freebies

Revision ID: xxxxxx
Revises: 5f72c58bf48c
Create Date: 2023-03-15 15:06:20.944586

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxx'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id')),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id')),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('freebies')