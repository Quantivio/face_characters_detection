# Face Detection API

A simple face detection API made with Python Flask and FastAPI, using the Deepface library.

## Tech Stack

- Python
- Flask
- Deepface

## Dependencies

- Deepface: https://github.com/serengil/deepface

## Running the API

1. Clone the repository
2. Install the dependencies with Poetry:
    - Install Poetry
      with `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`
      or `pip install poetry`
    - Install the packages with `poetry install`
    - Start a poetry shell with `poetry shell`
3. Start the Flask development server with `flask run`
4. Start the FastAPI development server with `uvicorn fast_app:app`

## Installing Deepface on MacOS or Troubleshooting

If you encounter any errors during installation, try the following steps:

1. Remove the `pyproject.toml` and `poetry.lock` files
2. For MacOS with M1, run:
    - `poetry add tensorflow-macos tensorflow-Metal fastapi flask pillow`
3. Start a Poetry shell with `poetry shell`
4. Install Deepface without dependencies by running `pip install deepface --no-deps`

## Note

Before running the API, make sure to check that you have all the required dependencies installed and configured
correctly.
