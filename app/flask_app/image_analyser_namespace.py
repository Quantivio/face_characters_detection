from deepface import DeepFace
from flask import request
from flask_restx import Resource, Namespace
from werkzeug.datastructures import FileStorage

from app.schema import DataResponseSchema, ErrorResponseSchema
from app.utils import logger, image_saver

image_analyser_namespace = Namespace(
    "Deepface", description="Various Image Analysis Using Deepface"
)

request_parser = image_analyser_namespace.parser()
request_parser.add_argument(
    "image",
    type="FileStorage",
    location="files",
    required=True,
)


@image_analyser_namespace.route("/analyse", methods=["POST"])
class DeepfaceImageAnalyse(Resource):
    @staticmethod
    @image_analyser_namespace.expect(request_parser)
    def post():
        function_name: str = "Analyze Image - View"
        logger.info(function_name=function_name, message=f"Enter - {function_name}")
        try:
            response: FileStorage = request.files.get("image")
            analysis: list = DeepFace.analyze(image_saver(response))
            logger.info(function_name=function_name, message=f"Exit - {function_name}")
            return DataResponseSchema(
                message="Image analysed successfully",
                status="Ok",
                data=analysis,
            ).json()
        except (ValueError, FileNotFoundError, TypeError) as error:
            logger.error(
                function_name=function_name,
                message=f"Exit - {function_name} Exception Occurred: {error}",
            )
            return ErrorResponseSchema(
                message="Image analysing failed",
                status="Not Ok",
                error_details=str(error),
            ).json()
