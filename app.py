from flask import Flask, jsonify

app = Flask(__name__)

customers = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]


# Define a route to return the list of customers
@app.route('/customers', methods=['GET'])
@app.route('/customers/', methods=['GET'])
def get_customers():
    return jsonify(customers)

# Define a route to return a single customer by ID
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = next((c for c in customers if c["id"] == customer_id), None)
    if customer is not None:
        return jsonify(customer)
    else:
        return jsonify({"error": "Customer not found"}), 404

if __name__ == '__main__':
    app.run(debug=True , host="127.0.0.1", port=8081)
