from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from Services.ProductService import ProductService
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class ProductController(Resource):
    def get(self):
        prodService = ProductService()
        result = []
        for i in prodService.getProducts():
            nutList = []
            for j in i.nutInfList:
                nutList.append({
                    'name': j.name,
                    'quantity': j.quantity
                })
            result.append({
                'name': i.name,
                'price': i.price,
                'weight': i.weight,
                'nutInfList': nutList
            })
        jsonList = {'products': result}
        return jsonify(jsonList)  

api.add_resource(ProductController, '/products')

if __name__ == "__main__":
    app.run(port='3500')