from flask_smorest import abort

from flask.views import MethodView
from db import stores, items


# TODO validation
class StoreView(MethodView):
    stores = {}

    def post():
        item = request.get_json()
        item_uid = uuid.uuid4()
        item = {**item, "id": item_uid}
        items[item_uid] = item
        return item, 201

    def put(self, store_id, body: dict):

        return "wip"

    def delete(self, store_id):
        return "wip"

    def get(store_id):
        try:
            return stores["store_id"] in stores
        except KeyError:
            abort(404, message="Store not found")
