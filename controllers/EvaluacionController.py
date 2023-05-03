from flask import request
from flask_restful import Resource
from flask_cors import cross_origin
from models.Evaluacion import Cliente
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


class ClienteController(Resource):
    
    # Mostrando todos los clientes o un cliente por id
    @cross_origin()
    def get(self, idPrestatario=None):
        if idPrestatario:
            cliente = col.find_one({"idPrestatario": idPrestatario})
            if cliente:
                cliente['_id'] = str(cliente['_id'])
                return jsonify(cliente)
            else:
                return jsonify({"mensaje": "Evaluación no encontrada"})
        else:
            cursor = col.find()
            clientes = []
            for cliente in cursor:
                cliente['_id'] = str(cliente['_id'])
                clientes.append(cliente)
            return jsonify(clientes)
    #Creando un cliente
    @cross_origin()
    def post(self):
        json_data = request.get_json()
        result = col.insert_one(json_data)
        return {'message': 'Evaluación guardada exitosamente', '_id': str(result.inserted_id)}
    
    # def post(self):
    #     json_data = request.get_json()
    #     result = col.insert_one(json_data)
    #     return {'message': 'Cliente creado exitosamente', 'id_cliente': str(result.inserted_id)}
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
