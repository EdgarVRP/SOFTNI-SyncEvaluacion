import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from controllers.EvaluacionController import EvaluacionController
from flask import Flask


app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host='localhost', port=PORT)
    #se imprime en consola el puerto en el que se esta ejecutando la aplicacion

#Se muestra el mensaje de bienvenida
@app.route('/')
def hello_world():
    return 'Bienvenido a la API de Evaluaciones de Prestatarios'
#Se muestra el puerto en el que se esta ejecutando la aplicacion
@app.route('/port')
def port():
    return 'El puerto es: ' + str(PORT)

api = Api(app)
api.add_resource(EvaluacionController, "/Evaluaciones", "/Evaluaciones/<string:idPrestatario>")

