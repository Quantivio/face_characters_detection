from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource, Namespace

from app.config import AppConfig, PATH
from app.flask_app.image_analyser_namespace import image_analyser_namespace
from app.schema import CommonResponseSchema

app_config = AppConfig()

flask_app: Flask = Flask(__name__)
CORS(flask_app)
flask_app.config["UPLOAD_FOLDER"] = PATH
api = Api(flask_app, **app_config.api_kwargs)
health_check_namespace: Namespace = api.namespace(
    "Health Check",
    description="Used to verify the status of the flask app",
)


@health_check_namespace.route("/ping")
class HealthCheck(Resource):
    @staticmethod
    def get():
        return jsonify(
            CommonResponseSchema(
                message="Health check working fine", status="Ok"
            ).dict()
        )


api.add_namespace(image_analyser_namespace)

if __name__ == "__main__":
    flask_app.run()
