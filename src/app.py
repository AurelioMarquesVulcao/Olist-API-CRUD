from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId
from flask_cors import CORS
from decouple import config


app = Flask(__name__)

cors = CORS(app)

CORS(app)

# Uso de arquivo .env para proteger as variavéis
# Use of .env file to protect variables
DB = config('ACCESS_DB_OLIST', cast=str)
app.config['MONGO_URI'] = DB

mongo = PyMongo(app)


# metodo de envio de dados.
# method of sending data.
@app.route('/', methods=['POST'])
def create_user():
    name = request.json['name']
    name2 = request.json['name2']
    password = request.json['password']

    if name and name2 and password:
        hashed_password = generate_password_hash(password)
        # db.anydatas - anydatas é a minha base de dados
        id = mongo.db.anydatas.insert(
            {'name': name, 'name2': name2, 'password': hashed_password}
        )
        response = {
            'id': str(id),
            'name': name,
            'name2': name2,
            'password': hashed_password

        }
        return response
    else:
        return not_found()

    return {"message": "recebido"}


# metodo de recebimento de dados
@app.route('/', methods=['GET'])
def get_users():
    # a variavél que armazena pode ser qualquer nome que se encaixe na sua aplicação
    any_data = mongo.db.anydatas.find()
    # json util torna a resposta em algo util
    response = json_util.dumps(any_data)
    # Response do flask melhora a Resposta
    return Response(response, mimetype='application/json')




if __name__ == "__main__":
    # para produção desativar debug=True
    app.run(host='0.0.0.0', debug=True)