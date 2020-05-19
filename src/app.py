from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId
from flask_cors import CORS
# from decouple import config
import os


app = Flask(__name__)

cors = CORS(app)

CORS(app)

# Uso de arquivo .env para proteger as variavéis
# Use of .env file to protect variables
DB = config('mongodb+srv://Aurelioprod:U0PWxXrhk4KmFpp4@vulcaotech-pdii4.mongodb.net/Olist?retryWrites=true&w=majority')
app.config['MONGO_URI'] = DB

mongo = PyMongo(app)


# metodo de envio de dados.
# method of sending data.
@app.route('/authors', methods=['POST'])
def create_author():
    name = request.json['name']

    if name:
        id = mongo.db.anydatas.insert(
            {'name': name}
        )
        response = {
            'id': str(id),
            'name': name,
        }
        return response
    else:
        return not_found()

    return {"message": "recebido"}

    # metodo de recebimento de dados


@app.route('/author/<id>', methods=['GET'])
def get_author(id):
    any_data = mongo.db.authors.find({'_id': ObjectId(id)})
    response = json_util.dumps(any_data)
    return Response(response, mimetype='application/json')


@app.route('/books', methods=['GET'])
def get_books():
    any_data = mongo.db.books.find()
    response = json_util.dumps(any_data)
    return Response(response, mimetype='application/json')


@app.route('/books', methods=['POST'])
def create_books():
    name = request.json['name']
    publication_year = request.json['publication_year']
    edition = request.json['edition']
    author = request.json['author']

    if name and publication_year and edition and author:
        id = mongo.db.books.insert(
            {'name': name, 'publication_year': publication_year,
                'edition': edition, 'author': author}
        )
        response = {
            'id': str(id),
            'name': name,
            'publication_year': publication_year,
            'edition': edition,
            'author': author
        }
        return response
    else:
        return not_found()

    return {"message": "recebido"}


# @app.route('/books/<id>', methods=['GET'])
# def get_book_id(id):
#     any_data = mongo.db.books.find_one({'_id': ObjectId(id)})
#     response = json_util.dumps(any_data)
#     return Response(response, mimetype='application/json')



@app.route('/books/<name>', methods=['GET'])
def get_book_name(name):
    any_data = mongo.db.books.find({"name": name})
    response = json_util.dumps(any_data)
    return Response(response, mimetype='application/json')


@app.route('/<id>', methods=['DELETE'])
def delete_book(id):
    mongo.db.books.delete_one({'_id': ObjectId(id)})
    response = jsonify({"message": "User " + id + " was Deleted successfully"})
    return response


@app.route('/<id>', methods=['PUT'])
def update_book(id):
    name = request.json['name']
    name2 = request.json['name2']
    password = request.json['password']

    if name and publication_year and edition and author:
        mongo.db.books.update_one(
            {'_id': ObjectId(id)},
            {'$set': {
                'id': str(id),
                'name': name,
                'publication_year': publication_year,
                'edition': edition,
                'author': author
            }})
        response = jsonify(
            {"message": "User " + id + " was Update successfully"})
        return response


# para erros usuarios não encontrados ou problemas na base de dados
@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'Not Found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
