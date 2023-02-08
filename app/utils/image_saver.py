import os

from werkzeug.datastructures import FileStorage

from app.config.constants import PATH


def image_saver(response: FileStorage) -> str:
    random_name: str = os.urandom(8).hex()
    current_image_path: str = os.path.join(PATH, random_name + ".jpg")
    response.save(current_image_path)
    return current_image_path
