import os

from deepface import DeepFace
from flask import Flask, jsonify, request

PATH = '/run/media/vetrichelvan/Personal Workspace/My Projects/Minor Projects/Python Projects/Humain/images/'

app = Flask(__name__)


@app.route('/detect', methods=['POST'])
def recognize():
    response = request.files.get('image')
    randomName = os.urandom(8).hex()
    try:
        response.save(os.path.join(PATH, randomName + '.jpg'))
        analysis = DeepFace.analyze(os.path.join(PATH, randomName + '.jpg'))
        return jsonify(analysis)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()
