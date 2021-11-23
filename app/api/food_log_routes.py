from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import db, Food_Log, Breakfast, Lunch, Dinner
from datetime import datetime


food_log_routes = Blueprint('food_log_routes', __name__)


# Get Food_log
@food_log_routes.route('/<int:user_id>', methods=['GET'])
# @login_required
def get_food_log(user_id):

    user_breakfast = db.session.query(Breakfast).join(Food_Log).filter_by(user_id=user_id).add_entity(Food_Log).first()
    user_lunch = db.session.query(Lunch).join(Food_Log).filter_by(user_id=user_id).add_entity(Food_Log).first()
    user_dinner = db.session.query(Dinner).join(Food_Log).filter_by(user_id=user_id).add_entity(Food_Log).first()

    if not user_breakfast and not user_lunch and not user_dinner:
        return {'user_food_log': 'False'}

    # breakfast = [breakfast.to_dict() for breakfast in list(user_breakfast)]
    # lunch = [lunch.to_dict() for lunch in list(user_lunch)]
    # dinner = [dinner.to_dict() for dinner in list(user_dinner)]

    if not user_lunch and not user_dinner:
        breakfast = [breakfast.to_dict() for breakfast in list(user_breakfast)]
        return {'user_food_log': [{**breakfast[0], **breakfast[1]}]}

    if not user_dinner and not user_breakfast:
        lunch = [lunch.to_dict() for lunch in list(user_lunch)]
        return {'user_food_log': [{**lunch[0], **lunch[1]}]}

    if not user_breakfast and not user_lunch:
        dinner = [dinner.to_dict() for dinner in list(user_dinner)]
        return {'user_food_log': [{**dinner[0], **dinner[1]}]}

    if not user_breakfast:
        lunch = [lunch.to_dict() for lunch in list(user_lunch)]
        dinner = [dinner.to_dict() for dinner in list(user_dinner)]
        return {'user_food_log': [{**lunch[0], **lunch[1]}, {**dinner[0], **dinner[1]}]}

    if not user_lunch:
        breakfast = [breakfast.to_dict() for breakfast in list(user_breakfast)]
        dinner = [dinner.to_dict() for dinner in list(user_dinner)]
        return {'user_food_log': [{**breakfast[0], **breakfast[1]}, {**dinner[0], **dinner[1]}]}

    if not user_dinner:
        breakfast = [breakfast.to_dict() for breakfast in list(user_breakfast)]
        lunch = [lunch.to_dict() for lunch in list(user_lunch)]
        return {'user_food_log': [{**breakfast[0], **breakfast[1]}, {**lunch[0], **lunch[1]}]}

    breakfast = [breakfast.to_dict() for breakfast in list(user_breakfast)]
    lunch = [lunch.to_dict() for lunch in list(user_lunch)]
    dinner = [dinner.to_dict() for dinner in list(user_dinner)]

    return {'user_food_log': [{**breakfast[0], **breakfast[1]}, {**lunch[0], **lunch[1]}, {**dinner[0], **dinner[1]}]}


# Create new food log
@food_log_routes.route('/<int:user_id>', methods=['POST'])
# @login_required
def new_food_log(user_id):
    new_log = request.json
    current_log = Food_Log.query.filter_by(user_id=user_id, meal=new_log['meal']).first()

    print("\n\n\n\n new_log ============", new_log, "\n\n\n\n")
    print("\n\n\n\n current_log ============", current_log, "\n\n\n\n")


    if not current_log:
        nfl = Food_Log(
            name=new_log['name'],
            meal=new_log['meal'],
            user_id=new_log['user_id'],
            created_at=datetime.now())

        db.session.add(nfl)
        db.session.commit()

        #******** Issue with not being able to grab Food_Log ID after it's been instantiated. **************

        log = Food_Log.query.filter_by(user_id=user_id, meal=new_log['meal']).first()
        print("\n\n\n\n log=============", log, "\n\n\n\n")

        nb = Breakfast(
            calories=new_log['calories'],
            carbohydrates=new_log['carbohydrates'],
            fat=new_log['fat'],
            protein=new_log['protein'],
            foodlog_id=log.to_dict()['id'],
            daily_nutrition_goals_id=new_log["daily_nutrition_goals_id"])

        db.session.add(nb)
        db.session.commit()

    user_breakfast = db.session.query(Breakfast).join(Food_Log).filter_by(user_id=user_id).add_entity(Food_Log).first()
    user_lunch = db.session.query(Lunch).join(Food_Log).filter_by(user_id=user_id).add_entity(Food_Log).first()
    user_dinner = db.session.query(Dinner).join(Food_Log).filter_by(user_id=user_id).add_entity(Food_Log).first()

    if not user_breakfast and not user_lunch and not user_dinner:
        return {'user_food_log': 'False'}

    # breakfast = [breakfast.to_dict() for breakfast in list(user_breakfast)]
    # lunch = [lunch.to_dict() for lunch in list(user_lunch)]
    # dinner = [dinner.to_dict() for dinner in list(user_dinner)]

    if not user_lunch and not user_dinner:
        breakfast = [breakfast.to_dict() for breakfast in list(user_breakfast)]
        return {'user_food_log': [{**breakfast[0], **breakfast[1]}]}

    if not user_dinner and not user_breakfast:
        lunch = [lunch.to_dict() for lunch in list(user_lunch)]
        return {'user_food_log': [{**lunch[0], **lunch[1]}]}

    if not user_breakfast and not user_lunch:
        dinner = [dinner.to_dict() for dinner in list(user_dinner)]
        return {'user_food_log': [{**dinner[0], **dinner[1]}]}

    if not user_breakfast:
        lunch = [lunch.to_dict() for lunch in list(user_lunch)]
        dinner = [dinner.to_dict() for dinner in list(user_dinner)]
        return {'user_food_log': [{**lunch[0], **lunch[1]}, {**dinner[0], **dinner[1]}]}

    if not user_lunch:
        breakfast = [breakfast.to_dict() for breakfast in list(user_breakfast)]
        dinner = [dinner.to_dict() for dinner in list(user_dinner)]
        return {'user_food_log': [{**breakfast[0], **breakfast[1]}, {**dinner[0], **dinner[1]}]}

    if not user_dinner:
        breakfast = [breakfast.to_dict() for breakfast in list(user_breakfast)]
        lunch = [lunch.to_dict() for lunch in list(user_lunch)]
        return {'user_food_log': [{**breakfast[0], **breakfast[1]}, {**lunch[0], **lunch[1]}]}

    breakfast = [breakfast.to_dict() for breakfast in list(user_breakfast)]
    lunch = [lunch.to_dict() for lunch in list(user_lunch)]
    dinner = [dinner.to_dict() for dinner in list(user_dinner)]

    return {'user_food_log': [{**breakfast[0], **breakfast[1]}, {**lunch[0], **lunch[1]}, {**dinner[0], **dinner[1]}]}


# Update current food log
@food_log_routes.route('/<int:user_id>', methods=['PUT'])
# @login_required
def update_food_log(user_id):
    updated_log = request.json
    current_log = Food_Log.query.filter_by(user_id=user_id, meal=updated_log['meal']).first()
    # print("\n\n\n\n", request.json, "\n\n\n\n")
    # print("\n\n\n\n", current_log, "\n\n\n\n")
    if current_log:
        current_log.name = updated_log['name'],
        current_log.created_at = datetime.now()
        db.session.commit()

    user_breakfast = db.session.query(Breakfast).join(Food_Log).filter_by(user_id=user_id).add_entity(Food_Log).first()
    user_lunch = db.session.query(Lunch).join(Food_Log).filter_by(user_id=user_id).add_entity(Food_Log).first()
    user_dinner = db.session.query(Dinner).join(Food_Log).filter_by(user_id=user_id).add_entity(Food_Log).first()

    if not user_breakfast and not user_lunch and not user_dinner:
        return {'user_food_log': 'False'}

    breakfast = [breakfast.to_dict() for breakfast in list(user_breakfast)]
    lunch = [lunch.to_dict() for lunch in list(user_lunch)]
    dinner = [dinner.to_dict() for dinner in list(user_dinner)]


    if not user_breakfast:
        return {'user_food_log': [{**lunch[0], **lunch[1]}, {**dinner[0], **dinner[1]}]}

    if not user_breakfast and not user_lunch:
        return {'user_food_log': [{**dinner[0], **dinner[1]}]}

    if not user_lunch:
        return {'user_food_log': [{**breakfast[0], **breakfast[1]}, {**dinner[0], **dinner[1]}]}

    if not user_lunch and not user_dinner:
        return {'user_food_log': [{**breakfast[0], **breakfast[1]}]}

    if not user_dinner:
        return {'user_food_log': [{**breakfast[0], **breakfast[1]}, {**lunch[0], **lunch[1]}]}

    if not user_dinner and not user_breakfast:
        return {'user_food_log': [{**lunch[0], **lunch[1]}]}

    return {'user_food_log': [{**breakfast[0], **breakfast[1]}, {**lunch[0], **lunch[1]}, {**dinner[0], **dinner[1]}]}

# delete food_log
@food_log_routes.route('/<int:user_id>', methods=['DELETE'])
# @login_required
def delete_food_log(user_id):
    food_log = Food_Log.query.filter_by(user_id=user_id).all()
    # db.session.commit()
    for log in food_log:
        if log.to_dict()['meal'] == 'breakfast':
            Breakfast.query.filter_by(foodlog_id=log.to_dict()['id']).delete()
            Food_Log.query.filter_by(user_id=user_id, meal='breakfast').delete()
            db.session.commit()

        if log.to_dict()['meal'] == 'lunch':
            Lunch.query.filter_by(foodlog_id=log.to_dict()['id']).delete()
            Food_Log.query.filter_by(user_id=user_id, meal='lunch').delete()
            db.session.commit()

        if log.to_dict()['meal'] == 'dinner':
            Dinner.query.filter_by(foodlog_id=log.to_dict()['id']).delete()
            Food_Log.query.filter_by(user_id=user_id, meal='dinner').delete()
            db.session.commit()

    return {'food-log': 'False'}