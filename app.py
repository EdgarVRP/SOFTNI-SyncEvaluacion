import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from controllers.EvaluacionController import EvaluacionController
from flask import Flask


app = Flask(__name__)
CORS(app)

api = Api(app)
api.add_resource(EvaluacionController, "/Evaluaciones", "/Evaluaciones/<string:idPrestatario>")

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5001))
    app.run(host='localhost', port=PORT, debug=True)