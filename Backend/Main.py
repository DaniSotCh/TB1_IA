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
            result.append({
                'Name': i.name,
                'Price(s/.)': i.price,
                'Weight(1-5)': i.weight,
                'Calories(kcal)': i.calories,
                'Fat(g)': i.fat,
                'Carbs(g)': i.carbs,
                'Protein(g)': i.protein
            })
        return jsonify(result) 
class BasketController(Resource):
    def get(self):
        args = request.args
        print (args) # For debugging
        familyType = args['familyType']
        cost = float(args['cost'])
        postSA =  ProductService()
        result = postSA.postSimulatedAnnealing(cost, familyType)
        
        return jsonify(result) 

api.add_resource(ProductController, '/products')
api.add_resource(BasketController, '/bestbasket')

if __name__ == "__main__":
    app.run(port='3500')