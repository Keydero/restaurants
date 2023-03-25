from db import db


class OwnerModel(db.model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    restaurant = db.relationship("RestaurantModel", back_populate="restaurants", lazy="dynamic")
