import json
from flask import Flask, jsonify, request

class Product:
    def __init__(self):
        self.products = [
            {'id' : 1, 'Product' : 'Zabers'}
        ]
        self.NEXT_ID = 2
    def incr_next_id(self):
        self.NEXT_ID += 1
        return
    def get_index(self, id):
        for i in range(len(self.products)):
            if self.products[i]['id'] == id:
                return i
        return -1
    def get_info(self, id):
        for i in self.products:
            if i['id'] == id:
                return i
        return None
    def get_product(self, id):
        return self.get_info(id)['Product']
    def add_product(self, item):
        self.products.append({'id' : self.NEXT_ID, 'Product' : item})
        self.incr_next_id()
        return self.products[-1]
    def remove_product(self, id):
        for i in self.products:
            if i['id'] == id:
                self.products.remove(i)
                return True
        return False
    def modify_product(self, id, name):
        position = self.get_index(id)
        if position == -1:
            return None
        self.products[position]['Product'] = name
        return self.products[position]

new_products = Product()
app = Flask(__name__)

#curl -v http://localhost:5000/products
@app.route('/products')
def get_products():
    return jsonify(new_products.products)

#curl -v http://localhost:5000/product/1
@app.route('/product/<int:id>')
def get_product(id):
    find_prod = new_products.get_info(id)
    if not find_prod:
        return f'Product with id {id} not found', 404
    return jsonify(find_prod)

#curl --header "Content-Type: application/json" --request POST --data '{'Product': 'some product'} -v http://localhost:5000/product/
@app.route('/product', methods=['POST'])
def post_product():
    request_item = request.json
    return jsonify(new_products.add_product(request_item['Product'])), 201

#curl --header "Content-Type: application/json" --request PUT --data '{'Product': 'some product'} -v http://localhost:5000/product/2
@app.route('/product/<int:id>', methods=['PUT'])
def put_product(id):
    updated = request.json
    modify = new_products.modify_product(id, updated['Product'])
    if modify == -1:
        return f'Product with id {id} not found', 404
    return jsonify(modify), 200

#curl --request DELETE -v http://localhost:500/product/2
@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    try_remove = new_products.remove_product(id)
    if try_remove:
        return f'Product with id {id} deleted', 200
    return f'Product with id {id} not found', 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')