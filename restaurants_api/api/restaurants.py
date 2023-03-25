#import uuid
#from flask import request


from schemas import RestaurantSchema

from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("restaurants", __name__, description="Restaurants crud")


@blp.route("/restaurants/<string:restaurant_id>")
class RestaurantView(MethodView):
    def get(self,restaurant_id):
        return restaurant_id

    @blp.arguments(RestaurantSchema)
    @blp.response(201, RestaurantSchema(many=True))
    def post(self, restaurant):
        return restaurant
