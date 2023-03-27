# import uuid
# from flask import request
# import uuid
# from flask import request
from opentelemetry import trace
from opentelemetry.trace import SpanKind
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource
from schemas import RestaurantSchema
from opentelemetry.semconv.trace import HttpFlavorValues, SpanAttributes
from flask_smorest import Blueprint, abort
from flask.views import MethodView

from .resource_detector import LocalMachineResourceDetector

local_resource = LocalMachineResourceDetector().detect()
resource = local_resource.merge(
    Resource.create({
        "service.name": "restaurants",
        "service.version": "0.0.1"
    })
)

trace.set_tracer_provider(TracerProvider(resource=resource))

otlp_exporter = OTLPSpanExporter(endpoint="opentelemetry-collector:4317", insecure=True)


trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

tracer = trace.get_tracer(__name__)

blp = Blueprint("restaurants", __name__, description="Restaurants crud")


@blp.route("/restaurants/<string:restaurant_id>")
class RestaurantView(MethodView):

    def get(self, restaurant_id):
        with tracer.start_as_current_span("server_request", attributes={"endpoint": f'restaurants/{restaurant_id}'},
                                          kind=trace.SpanKind.CLIENT):
            with tracer.start_as_current_span("another_span", attributes={"endpoint": f'restaurants/{restaurant_id}'}):
                span = trace.get_current_span()
                span.set_attributes(
                    {
                        SpanAttributes.HTTP_METHOD: "GET"
                    }
                )
                return restaurant_id

    @blp.arguments(RestaurantSchema)
    @blp.response(201, RestaurantSchema(many=True))
    def post(self, restaurant):
        return restaurant
