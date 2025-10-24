# Import the jsonify function from Flask 
# (used to return JSON-formatted responses)
from flask import jsonify


# Define a helper function 'error' to create a consistent error response
def error(message): 
    # Return a JSON response with "status" and "message" keys, 
    # along with an HTTP status code 400 (Bad Request)
    return jsonify({"status": "error", "message": message}), 400


# Check if all required fields exist
def validate_required_fields(data):
    # Define which fields are mandatory in the input data
    fields = ["name", "unit_price", "quantity"]
    # If no data is provided OR any required field is missing
    if not data or any(item not in data for item in fields):
        # Return an error message about missing required fields
        return error("Missing required fields: name, quantity, unit_price")


# Check data types for each field
def validate_data_types(data):
    # If "name" is not a string return error
    if not isinstance(data["name"], str): 
        return error("Name must be a string")
    # If "unit_price" is not a number (int or float) return error
    if not isinstance(data["unit_price"], (int, float)): 
        return error("Unit price must be a number")
    # If "quantity" is not an integer → return error
    if not isinstance(data["quantity"], int): 
        return error("Quantity must be an integer")


# Ensure 'name' is not empty or just spaces
def validate_non_empty_name(data):
    # If the name field is empty after stripping spaces
    if not data["name"].strip():
        # Return error message for empty name
        return error("Name field cannot be empty")


# Ensure numeric fields are positive values
def validate_positive_values(data):
    # If either quantity or unit_price is 0 or negative
    if data["quantity"] <= 0 or data["unit_price"] <= 0:
        # Return an error message about invalid values
        return error("Quantity and Unit Price must be greater than zero")


# Check if the item name already exists in stock list
def check_duplicate_name(stock_list, name):
    # Iterate over all items and compare names (case-insensitive)
    if any(New_Item["name"].lower() == name.lower() for New_Item in stock_list):
        # If a duplicate name is found, return an error
        return error(f"Item '{name}' already exists")
