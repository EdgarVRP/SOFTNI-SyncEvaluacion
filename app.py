from flask import Flask
from flask_restful import Api
from controllers.EvaluacionController import ClienteController

app = Flask(__name__)
api = Api(app)

api.add_resource(ClienteController, "/Evaluaciones", "/Evaluaciones/<string:id_cliente>")
