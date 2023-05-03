from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from controllers.EvaluacionController import ClienteController
from flask import Flask


app = Flask(__name__)
CORS(app)

api = Api(app)
api.add_resource(ClienteController, "/Evaluaciones", "/Evaluaciones/<string:idPrestatario>")
