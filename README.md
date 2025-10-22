# Flask Stock Management API

## Overview
This is a simple **Flask-based RESTful API** that demonstrates basic **CRUD operations** (Create, Read, Update, Delete) for managing a small stock inventory.  
The data is stored **in-memory** (using a Python list), making it ideal for learning or prototyping.

---

## Features
- **Create** a new stock item  
- **Retrieve** all or individual stock records  
- **Update** existing stock items  
- **Delete** stock items  

Each stock item contains:
```json
{
  "id": 1,
  "name": "Rice",
  "quantity": 10,
  "unit_price": 65000,
  "total_price": 650000,
  "description": "50kg bag of rice"
}
```

---

## Technologies Used
- **Python 3.x**
- **Flask** (for building the API)
- **Postman** (for testing endpoints)

---

##  Setup Instructions

1. **Clone or download** this project folder to your system.

2. **Navigate** into the project directory:
   ```bash
   cd your_project_folder
   ```

3. **Create and activate** a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate        # Windows
   ```

4. **Install Flask**:
   ```bash
   pip install flask
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. The API will start running at:
   ```
   http://127.0.0.1:5000
   ```

---

##  Testing the Endpoints (with Postman)

### 1. Retrieve Stocks (GET)
- **URL:** `http://127.0.0.1:5000/retrieve/stocks/1`
- **Method:** GET  
- **Response Example:**
  ```json
  [
    {
      "id": 1,
      "name": "Rice",
      "quantity": 10,
      "unit_price": 65000,
      "total_price": 650000,
      "description": "50kg bag of rice"
    }
  ]
  ```

---

### 2. Create a New Stock (POST)
- **URL:** `http://127.0.0.1:5000/create/stocks/1`
- **Method:** POST  
- **Body (raw JSON):**
  ```json
  {
    "name": "Beans",
    "quantity": 5,
    "unit_price": 30000,
    "description": "25kg bag of beans"
  }
  ```
- **Response:**
  ```json
  {
    "id": 2,
    "name": "Beans",
    "quantity": 5,
    "unit_price": 30000,
    "total_price": 150000,
    "description": "25kg bag of beans"
  }
  ```

---

### 3. Update a Stock (PUT)
- **URL:** `http://127.0.0.1:5000/update/stocks/1`
- **Method:** PUT  
- **Body (raw JSON):**
  ```json
  {
    "quantity": 20,
    "description": "Updated 50kg bag of rice"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Stock updated successfully",
    "updated_stock": {
      "id": 1,
      "name": "Rice",
      "quantity": 20,
      "unit_price": 65000,
      "total_price": 1300000,
      "description": "Updated 50kg bag of rice"
    }
  }
  ```

---

### 4. Delete a Stock (DELETE)
- **URL:** `http://127.0.0.1:5000/delete/stocks/1`
- **Method:** DELETE  
- **Response:**
  ```json
  {
    "message": "Stock deleted successfully"
  }
  ```

---

## Notes
- All data is **stored in memory**, meaning it will reset when you restart the server.
- To make the data persistent, you could later connect this API to a **database** like SQLite or MySQL.
- For learning purposes, this project helps you understand how RESTful APIs work in Flask.

---

## Author
**Name:** Fashola Joshua Temiloluwa  
