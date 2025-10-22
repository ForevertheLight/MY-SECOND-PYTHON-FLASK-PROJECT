# Import necessary modules from Flask
from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# IN-MEMORY DATA STORE 

# A list that stores stock information in memory
# (acts like a temporary database)
Stock = [
    # {"id": 1, "name": "Rice", "quantity": 10, "unit_price": 65000,
    #  "total_price": 650000, "description": "50kg bag of rice"}
]

# A simple counter for tracking stock IDs (not used much here)
Stock_Counter = 1


# READ: RETRIEVE STOCKS 

# Define a GET endpoint to retrieve stock data
@app.route("/retrieve/stocks/<int:Stock_ID>", methods=['GET'])
def retrieve_stocks(Stock_ID):
    # Check if the stock list is empty
    if not Stock:
        return "Empty Stock"
    
    # Return the list of all stocks
    return Stock


# CREATE: ADD NEW STOCK 

# Define a POST endpoint to create a new stock item
@app.route("/create/stocks/<int:Stock_ID>", methods=['POST'])
def create_new_stock(Stock_ID):
    # Use 'global' to modify the global counter variable
    global Stock_Counter

    # Extract JSON data from the request body
    data = request.get_json()

    #Validate Required fields 
    if not data or "name" not in data or "unit_price" not in data or "quantity" not in data:
        return jsonify({
            "Status":"Error",
            "Message":"Missing Required Fields: Name, Quantity, Unit_price"
            }),400
    
    # Create a new stock dictionary from the input data
    New_stock = {
        "id": len(Stock) + 1,  # Automatically generate new ID
        'name': data['name'],  # Stock name (required)
        'quantity': data.get('quantity', 1),  # Default quantity = 1
        'unit_price': data['unit_price'],  # Unit price (required)
        'description': data.get('description', ''),  # Optional description
        'total_price': data['quantity'] * data['unit_price']  # Auto-calculate total
    }

    # Add the new stock item to the in-memory list
    Stock.append(New_stock)

    # Return the newly added stock as a response
    return New_stock


# UPDATE: MODIFY EXISTING STOCK 

# Define a PUT endpoint to update an existing stock item
@app.route("/update/stocks/<int:Stock_ID>", methods=['PUT'])
def update_stock(Stock_ID):
    # Extract JSON data from the request body
    data = request.get_json()

    # Loop through all stock items
    for item in Stock:
        # Find the item with the matching ID
        if item["id"] == Stock_ID:
            # Update each field if a new value is provided
            item['name'] = data.get('name', item['name'])
            item['quantity'] = data.get('quantity', item['quantity'])
            item['unit_price'] = data.get('unit_price', item['unit_price'])
            item['description'] = data.get('description', item['description'])
            
            # Recalculate total price after update
            item['total_price'] = item['quantity'] * item['unit_price']
            
            # Return success message and updated stock
            return jsonify({
                "message": "Stock updated successfully",
                "updated_stock": item
            })
    
    # If the stock ID does not exist, return a 404 error
    return jsonify({"error": "Stock not found"}), 404


# DELETE: REMOVE A STOCK

# Define a DELETE endpoint to remove a stock item
@app.route("/delete/stocks/<int:stock_id>", methods=['DELETE'])
def delete_stock(stock_id):
    # Loop through the list of stock items
    for item in Stock:
        # Find the one with the matching ID
        if item["id"] == stock_id:
            # Remove it from the list
            Stock.remove(item)
            # Return a success message
            return jsonify({"message": "Stock deleted successfully"})
    
    # If no matching stock found, return an error
    return jsonify({"error": "Stock not found"}), 404
