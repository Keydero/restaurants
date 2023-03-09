
from flask_smorest import abort
from connexion import request
from flask.views import MethodView
import uuid
from db import stores, items

class StoreView(MethodView):
    stores = {}

    def post():
        # validation wip
        new_store = request.get_json()
        store_uid = uuid.uuid4()
        store = {**new_store, "id": store_uid}
        stores[store_uid] = store
        return store, 201

    def put(self, store_id, body: dict):

        return "wip"

    def delete(self, store_id):
        return "wip"

    def get(store_id):
        try:
            return stores["store_id"] in stores
        except KeyError:
            abort(404, message="Store not found")

