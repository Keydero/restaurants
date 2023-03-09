from flask_smorest import abort
from connexion import request
from flask.views import MethodView
import uuid
from db import items


class ItemView(MethodView):
    items = {}

    def post():
        # validation wip
        item = request.get_json()
        item_uid = uuid.uuid4()
        item = {**item, "id": item_uid}
        items[item_uid] = item
        return item, 201

    def put():

        return "wip"

    def delete():
        return "wip"

    def get():
        try:
            return ""
        except KeyError:
            abort(404, message="Item not found")
