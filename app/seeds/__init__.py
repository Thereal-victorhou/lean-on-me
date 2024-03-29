from flask.cli import AppGroup
from .users import seed_users, undo_users
from .daily_nutrition_goals import seed_daily_nutrition_goals, undo_daily_nutrition_goals
from .food_log import seed_food_log, undo_food_log
from .breakfast import seed_breakfast, undo_breakfast
from .lunch import seed_lunch, undo_lunch
from .dinner import seed_dinner, undo_dinner
from .favorite_foods import seed_favorite_foods, undo_favorite_foods
from app.models.db import db, environment, SCHEMA


# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding, truncate all tables prefixed with schema name
        db.session.execute(f'TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;')
        db.session.execute(f'TRUNCATE table {SCHEMA}.daily_nutrition_goals RESTART IDENTITY CASCADE;')
        db.session.execute(f'TRUNCATE table {SCHEMA}.food_log RESTART IDENTITY CASCADE;')
        db.session.execute(f'TRUNCATE table {SCHEMA}.breakfast RESTART IDENTITY CASCADE;')
        db.session.execute(f'TRUNCATE table {SCHEMA}.lunch RESTART IDENTITY CASCADE;')
        db.session.execute(f'TRUNCATE table {SCHEMA}.dinner RESTART IDENTITY CASCADE;')
        db.session.execute(f'TRUNCATE table {SCHEMA}.favorite_foods RESTART IDENTITY CASCADE;')
        db.session.commit()
    seed_users()
    seed_daily_nutrition_goals()
    seed_food_log()
    seed_breakfast()
    seed_lunch()
    seed_dinner()
    seed_favorite_foods()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_daily_nutrition_goals()
    undo_food_log()
    undo_breakfast()
    undo_lunch()
    undo_dinner()
    undo_favorite_foods()
    # Add other undo functions here
