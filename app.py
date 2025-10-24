# Import necessary modules from Flask
from flask import Flask, request, jsonify

from input_validations import (
    validate_required_fields,
    validate_data_types,
    validate_non_empty_name,
    validate_positive_values,
    check_duplicate_name
)


# Create a Flask application instance
app = Flask(__name__)

# IN-MEMORY DATA STORE 

# A list that stores stock information in memory
# (acts like a temporary database)
Stock = [ ]

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

@app.route("/create/stocks", methods=['POST'])
def create_new_stock():
    data = request.get_json()

    # Run all validations
    errors = (
        validate_required_fields(data)
        or validate_data_types(data)
        or validate_non_empty_name(data)
        or validate_positive_values(data)
        or check_duplicate_name(Stock, data["name"])
    )
    if errors:
        return errors  # Return the first error found

    # Create new stock entry
    new_stock = {
        "id": len(Stock) + 1,
        "name": data["name"],
        "quantity": data.get("quantity", 1),
        "unit_price": data["unit_price"],
        "description": data.get("description", ""),
        "total_price": data["quantity"] * data["unit_price"],
    }

    # Save and return response
    Stock.append(new_stock)
    return jsonify({
        "status": "success",
        "message": "New item added successfully",
        "stock": new_stock
    }), 201


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
