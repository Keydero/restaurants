#import uuid
#from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("restaurants", __name__, description="Restaurants crud")


@blp.route("/restaurants/<string:restaurant_id>")
class RestaurantView(MethodView):
    def get(self,restaurant_id):
        return restaurant_id
