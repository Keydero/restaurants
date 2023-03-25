from flask import Flask, request
from flask_smorest import Api
from api.restaurants import blp as RestaurantBlueprint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Restaurants REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.0"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.19.5/"



api = Api(app)


api.register_blueprint(RestaurantBlueprint)

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000, debug=True)

