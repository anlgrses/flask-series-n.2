from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)

items = []


class Item(Resource):
     def get(self, name):
         item = next(filter(lambda x: x["name"] == name, items), None)
         return {"item" : item}, 200 if item is not None else 404

     def post(self, name):
         data = request.get_json()
         item = {"name" : name, "price" : data['price']}
         items.append(item)   
         return item, 201



class itemList(Resource):
    def get(self):
        return {"items": items
        
        
api.add_resource(itemList, '/items')
api.add_resource(Item, '/item/<string:name>')

app.run(port=8080, debug=True)