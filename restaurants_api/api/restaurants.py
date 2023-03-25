# import uuid
# from flask import request

from opentelemetry.sdk.resources import Resource
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, BatchSpanProcessor
from schemas import RestaurantSchema

from flask.views import MethodView
from flask_smorest import Blueprint, abort


def configure_tracer():
    resource = Resource.create({
        "service.name": "restaurants",
        "service.version": "0.0.1"
    })
    exporter = ConsoleSpanExporter()
    span_processor = BatchSpanProcessor(exporter)
    provider = TracerProvider(resource=resource)
    provider.add_span_processor(span_processor)
    trace.set_tracer_provider(provider)

    return trace.get_tracer("restaurants.py", "0.0.1")


tracer = configure_tracer()
blp = Blueprint("restaurants", __name__, description="Restaurants crud")


@blp.route("/restaurants/<string:restaurant_id>")
class RestaurantView(MethodView):

    def get(self, restaurant_id):
        with tracer.start_as_current_span("server_request", attributes={"endpoint": f'restaurants/{restaurant_id}'}):
            with tracer.start_as_current_span("another_span", attributes={"endpoint": f'restaurants/{restaurant_id}'}):
                return restaurant_id

    @blp.arguments(RestaurantSchema)
    @blp.response(201, RestaurantSchema(many=True))
    def post(self, restaurant):
        return restaurant
