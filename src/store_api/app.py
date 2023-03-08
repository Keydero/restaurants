import connexion
from connexion.resolver import RestyResolver
app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", resolver=RestyResolver('api'), port=8000, debug=True)
