# Face Detection API

A simple face detection API made with Python and Flask, using the Deepface library.

## Tech Stack

- Python
- Flask
- Deepface

## Dependencies
- Deepface: https://github.com/serengil/deepface

## Running the API
1. Clone the repository
2. Install the dependencies with Poetry:
    - Install Poetry with `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python` or `pip install poetry`
    - Install the packages with `poetry install`
    - To spawn a new shell run `poetry shell` 
3. Start the Flask development server with `flask run`
4. Start the FastAPI development server with `uvicorn fast_app:app`

## Note
Before running the API, make sure to check that you have all the required dependencies installed and configured correctly.
