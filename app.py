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

