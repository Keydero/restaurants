from db import db


class RestaurantModel(db.model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    sir = db.Column(db.String(3), nullable=False)
    speciality = db.Column(db.String(30), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)
