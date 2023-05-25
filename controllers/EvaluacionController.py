from flask import request
from flask_restful import Resource
from flask_cors import cross_origin
from models.Evaluacion import Evaluacion
import pymongo
from dotenv import load_dotenv
import os
from flask import jsonify
load_dotenv()
uri = os.getenv("MONGODB_URI")
database = os.getenv("MONGODB_DATABASE")
collection = os.getenv("MONGODB_COLLECTION")
client = pymongo.MongoClient(uri)
db = client[database]
col = db[collection]
class EvaluacionController(Resource):
    # Mostrando todos los clientes o un cliente por id
    @cross_origin()
    def get(self, idPrestatario=None):
        if idPrestatario:
            Evaluacion = col.find_one({"idPrestatario": idPrestatario})
            if Evaluacion:
                Evaluacion['_id'] = str(Evaluacion['_id'])
                return jsonify(Evaluacion)
            else:
                return jsonify({"mensaje": "Evaluación no encontrada"})
        else:
            cursor = col.find()
            Evaluaciones = []
            for Evaluacion in cursor:
                Evaluacion['_id'] = str(Evaluacion['_id'])
                Evaluaciones.append(Evaluacion)
            return jsonify(Evaluaciones)
    #Creando un cliente
    @cross_origin()
    def post(self):
        json_data = request.get_json()
        result = col.insert_one(json_data)
        return {'message': 'Evaluación guardada exitosamente', '_id': str(result.inserted_id)}
    @cross_origin()
    def put(self, idPrestatario):
        json_data = request.get_json()
        result = col.update_one({'idPrestatario': idPrestatario}, {'$set': json_data})
        if result.modified_count == 0:
            return {'message': 'Evaluación no encontrada'}, 404
        else:
            return {'message': 'Evaluación actualizada exitosamente'}    
    @cross_origin()
    def delete(self, idPrestatario):
        result = col.delete_one({'idPrestatario': idPrestatario})
        if result.deleted_count == 0:
            return {'message': 'Evaluación no encontrada'}, 404
        else:
            return {'message': 'Evaluación eliminada exitosamente'}