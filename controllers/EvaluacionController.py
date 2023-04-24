from flask import request
from flask_restful import Resource
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
    def get(self, id_cliente=None):
        if id_cliente:
            cliente = col.find_one({"id_cliente": id_cliente})
            if cliente:
                cliente['_id'] = str(cliente['_id'])
                return jsonify(cliente)
            else:
                return jsonify({"mensaje": "Cliente no encontrado"})
        else:
            cursor = col.find()
            clientes = []
            for cliente in cursor:
                cliente['_id'] = str(cliente['_id'])
                clientes.append(cliente)
            return jsonify(clientes)
    #Creando un cliente
    def post(self):
        json_data = request.get_json()
        result = col.insert_one(json_data)
        return {'message': 'Cliente creado exitosamente', '_id': str(result.inserted_id)}
    
    # def post(self):
    #     json_data = request.get_json()
    #     result = col.insert_one(json_data)
    #     return {'message': 'Cliente creado exitosamente', 'id_cliente': str(result.inserted_id)}

    def put(self, id_cliente):
        json_data = request.get_json()
        result = col.update_one({'id_cliente': id_cliente}, {'$set': json_data})
        if result.modified_count == 0:
            return {'message': 'Cliente no encontrado'}, 404
        else:
            return {'message': 'Cliente actualizado exitosamente'}

    def delete(self, id_cliente):
        result = col.delete_one({'id_cliente': id_cliente})
        if result.deleted_count == 0:
            return {'message': 'Cliente no encontrado'}, 404
        else:
            return {'message': 'Cliente eliminado exitosamente'}
