from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for investment funds
funds = []

# Endpoint to retrieve a list of all funds
@app.route('/funds', methods=['GET'])
def get_all_funds():
    return jsonify(funds), 200

# Endpoint to create a new fund
@app.route('/funds', methods=['POST'])
def create_fund():
    new_fund = request.json
    funds.append(new_fund)
    return jsonify({"message": "Fund created successfully!", "fund": new_fund}), 201

# Endpoint to retrieve details of a specific fund using its ID
@app.route('/funds/<int:fund_id>', methods=['GET'])
def get_fund_by_id(fund_id):
    for fund in funds:
        if fund['fund_id'] == fund_id:
            return jsonify(fund), 200
    return jsonify({"error": "Fund not found"}), 404

# Endpoint to update the performance of a fund using its ID
@app.route('/funds/<int:fund_id>', methods=['PUT'])
def update_fund_performance(fund_id):
    data = request.json
    for fund in funds:
        if fund['fund_id'] == fund_id:
            fund['fund_performance'] = data.get('fund_performance', fund['fund_performance'])
            return jsonify({"message": "Fund performance updated successfully!", "fund": fund}), 200
    return jsonify({"error": "Fund not found"}), 404

# Endpoint to delete a fund using its ID
@app.route('/funds/<int:fund_id>', methods=['DELETE'])
def delete_fund(fund_id):
    global funds
    funds = [fund for fund in funds if fund['fund_id'] != fund_id]
    return jsonify({"message": "Fund deleted successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
