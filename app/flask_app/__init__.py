from flask import Flask
from flask_restx import Api

from app.config import AppConfig, PATH
from app.flask_app.image_analyser_namespace import image_analyser_namespace

app_config = AppConfig()

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = PATH
api = Api(app, **app_config.api_kwargs)

api.add_namespace(image_analyser_namespace)

if __name__ == "__main__":
    app.run()
