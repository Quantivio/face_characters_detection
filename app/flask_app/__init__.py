from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource

from app.config import AppConfig, PATH
from app.flask_app.image_analyser_namespace import image_analyser_namespace
from app.schema import CommonResponseSchema

app_config = AppConfig()

app = Flask(__name__)
CORS(app)
app.config["UPLOAD_FOLDER"] = PATH
api = Api(app, **app_config.api_kwargs)


@api.route("/ping")
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
    app.run()
