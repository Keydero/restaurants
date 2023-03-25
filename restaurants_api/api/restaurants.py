#import uuid
#from flask import request


from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
from schemas import RestaurantSchema

from flask.views import MethodView
from flask_smorest import Blueprint, abort


def configure_tracer():
    exporter = ConsoleSpanExporter()
    span_processor = SimpleSpanProcessor(exporter)
    provider = TracerProvider()
    provider.add_span_processor(span_processor)
    trace.set_tracer_provider(provider)

    return trace.get_tracer("restaurants.py", "0.0.1")


tracer = configure_tracer()
blp = Blueprint("restaurants", __name__, description="Restaurants crud")

@blp.route("/restaurants/<string:restaurant_id>")
class RestaurantView(MethodView):

    def get(self,restaurant_id):
        with tracer.start_as_current_span("server_request"):
            return restaurant_id

    @blp.arguments(RestaurantSchema)
    @blp.response(201, RestaurantSchema(many=True))
    def post(self, restaurant):
        return restaurant
