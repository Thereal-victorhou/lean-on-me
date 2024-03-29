from .db import db, environment, SCHEMA, add_prefix_for_prod

class Breakfast(db.Model):
    __tablename__ = "breakfast"
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    calories = db.Column(db.Integer, nullable=False)
    carbohydrates = db.Column(db.Integer, nullable=False)
    fat = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Integer, nullable=False)
    foodlog_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("food_log.id")), nullable=False)
    daily_nutrition_goals_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("daily_nutrition_goals.id"), ondelete='CASCADE'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "calories": self.calories,
            "carbohydrates": self.carbohydrates,
            "fat": self.fat,
            "protein": self.protein,
            "foodlog_id": self.foodlog_id,
            "daily_nutrition_goals_id": self.daily_nutrition_goals_id
        }

    food_log = db.relationship("Food_Log", back_populates="breakfast")
    daily_nutrition_goals = db.relationship("Daily_Nutrition_Goals", back_populates="breakfast")
