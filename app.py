from flask import Flask, request, jsonify

app=Flask(__name__)

#In memory store
Stock=[
    # {"id": 1, "name": "Rice", "quantity": 10, "unit_price": 65000,
    #   "total_price": 650000, "description": "50kg bag of rice"}
]
Stock_Counter=1

#retrieve all stocks
@app.route("/retrieve/stocks",methods=['GET'])
def retrieve_stocks():
    if not Stock:
        return "Empty Stock"
    return Stock

#Add a New Stock
@app.route("/create/stocks",methods=['POST'])
def create_new_stock():
    global Stock_Counter
    data=request.get_json()

    New_stock = {
        "id": len(Stock) + 1,
        'name': data['name'],
        'quantity': data.get('quantity', 1),
        'unit_price': data['unit_price'],
        'description': data.get('description', ''),
        'total_price': data['quantity'] * data['unit_price']
    }
    Stock.append(New_stock)
    return New_stock


# Update an existing stock
@app.route("/update/stocks/<int:Stock_ID>", methods=['PUT'])
def update_stock(Stock_ID):
    data=request.get_json()
    for item in Stock:
        if item["id"] == Stock_ID:
            item['name'] = data.get('name', item['name'])
            item['quantity'] = data.get('quantity', item['quantity'])
            item['unit_price'] = data.get('unit_price', item['unit_price'])
            item['description'] = data.get('description', item['description'])
            
            # Recalculate total price
            item['total_price'] = item['quantity'] * item['unit_price']
            
            return jsonify({"message": "Stock updated successfully", "updated_stock": item})
    
    return jsonify({"error": "Stock not found"}), 404


# Delete an existing stock
@app.route("/delete/stocks/<int:stock_id>", methods=['DELETE'])
def delete_stock(stock_id):
    for item in Stock:
        if item["id"] == stock_id:
            Stock.remove(item)
            return jsonify({"message": "Stock deleted successfully"})
    
    return jsonify({"error": "Stock not found"}), 404
