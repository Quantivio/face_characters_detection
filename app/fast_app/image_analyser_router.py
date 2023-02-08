import os

from deepface import DeepFace
from fastapi import APIRouter, UploadFile
from starlette.responses import JSONResponse

from app.config import PATH
from app.schema import DataResponseSchema, ErrorResponseSchema
from app.utils import logger

image_analyser_router: APIRouter = APIRouter(prefix="/deepface", tags=["Image Analyse"])


@image_analyser_router.post("/analyse")
async def analyse_image(file: UploadFile):
    function_name: str = "Analyse Image - Controller"
    try:
        file_name: str = os.urandom(8).hex() + ".jpg"
        with open(PATH + file_name, "wb") as image:
            image.write(await file.read())
        analysis: list = DeepFace.analyze(PATH + file_name)
        logger.info(function_name=function_name, message=f"Exit - {function_name}")
        return DataResponseSchema(
            message="Image analysed successfully",
            status="Ok",
            data=analysis,
        )
    except (ValueError, FileNotFoundError, TypeError) as error:
        logger.error(
            function_name=function_name,
            message=f"Exit - {function_name} Exception Occurred: {error}",
        )
        return JSONResponse(
            content=ErrorResponseSchema(
                message="Image analysing failed",
                status="Not Ok",
                error_details=str(error),
            ).dict(),
            status_code=500,
        )
