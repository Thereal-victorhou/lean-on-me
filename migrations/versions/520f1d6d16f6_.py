"""empty message

Revision ID: 520f1d6d16f6
Revises: 
Create Date: 2021-11-16 21:45:55.186047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '520f1d6d16f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('daily_nutrition_goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('calories', sa.Integer(), nullable=False),
    sa.Column('carbohydrates', sa.Integer(), nullable=False),
    sa.Column('fat', sa.Integer(), nullable=False),
    sa.Column('protein', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('food_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('food_type', sa.String(length=100), nullable=False),
    sa.Column('meal', sa.String(length=10), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('breakfast',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('calories', sa.Integer(), nullable=False),
    sa.Column('carbohydrates', sa.Integer(), nullable=False),
    sa.Column('fat', sa.Integer(), nullable=False),
    sa.Column('protein', sa.Integer(), nullable=False),
    sa.Column('foodlog_id', sa.Integer(), nullable=False),
    sa.Column('daily_nutrition_goals_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['daily_nutrition_goals_id'], ['daily_nutrition_goals.id'], ),
    sa.ForeignKeyConstraint(['foodlog_id'], ['food_log.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dinner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('calories', sa.Integer(), nullable=False),
    sa.Column('carbohydrates', sa.Integer(), nullable=False),
    sa.Column('fat', sa.Integer(), nullable=False),
    sa.Column('protein', sa.Integer(), nullable=False),
    sa.Column('foodlog_id', sa.Integer(), nullable=False),
    sa.Column('daily_nutrition_goals_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['daily_nutrition_goals_id'], ['daily_nutrition_goals.id'], ),
    sa.ForeignKeyConstraint(['foodlog_id'], ['food_log.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_foods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('foodlog_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['foodlog_id'], ['food_log.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lunch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('calories', sa.Integer(), nullable=False),
    sa.Column('carbohydrates', sa.Integer(), nullable=False),
    sa.Column('fat', sa.Integer(), nullable=False),
    sa.Column('protein', sa.Integer(), nullable=False),
    sa.Column('foodlog_id', sa.Integer(), nullable=False),
    sa.Column('daily_nutrition_goals_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['daily_nutrition_goals_id'], ['daily_nutrition_goals.id'], ),
    sa.ForeignKeyConstraint(['foodlog_id'], ['food_log.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lunch')
    op.drop_table('favorite_foods')
    op.drop_table('dinner')
    op.drop_table('breakfast')
    op.drop_table('food_log')
    op.drop_table('daily_nutrition_goals')
    op.drop_table('users')
    # ### end Alembic commands ###