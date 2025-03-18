from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Database file paths
FUNDS_DB_FILE = 'funds.db'
INVESTMENT_FUNDS_DB_FILE = 'investment_funds.db'


# Helper function to connect to the database
# Establish a database connection to the specified SQLite file
def get_db_connection(db_file):
    connection = sqlite3.connect(db_file)
    connection.row_factory = sqlite3.Row  # Enable row access via column names
    return connection


# Helper function to fetch data from a table
# Fetch all rows from a specified table in the SQLite database
def fetch_table_data(db_file, table_name):
    try:
        connection = get_db_connection(db_file)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        data = [dict(zip(column_names, row)) for row in rows]
        connection.close()
        return data
    except Exception as e:
        raise Exception(f"Failed to fetch data from {table_name}: {str(e)}")


# API Endpoints

# Fetch all data from the funds table in funds.db
@app.route('/funds', methods=['GET'])
def get_funds_from_funds_db():
    try:
        data = fetch_table_data(FUNDS_DB_FILE, 'funds')
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch data from funds.db", "details": str(e)}), 500

# Fetch all data from the funds table in investment_funds.db
@app.route('/investment-funds', methods=['GET'])
def get_funds_from_investment_funds_db():
    try:
        data = fetch_table_data(INVESTMENT_FUNDS_DB_FILE, 'funds')
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch data from investment_funds.db", "details": str(e)}), 500

# Add a new fund to the funds table in funds.db
@app.route('/funds/add', methods=['POST'])
def add_fund_to_funds_db():
    try:
        data = request.get_json()
        fund_name = data.get('fund_name')
        performance = data.get('performance')

        # Input validation
        if not fund_name or performance is None:
            return jsonify({"error": "Fund name and performance are required"}), 400

        connection = get_db_connection(FUNDS_DB_FILE)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO funds (fund_name, performance) VALUES (?, ?)", (fund_name, performance))
        connection.commit()
        connection.close()
        return jsonify({"message": f"Fund '{fund_name}' added successfully."}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "A fund with the given name already exists."}), 409
    except Exception as e:
        return jsonify({"error": "Failed to add fund to funds.db", "details": str(e)}), 500

# Delete a fund from the funds table in funds.db
@app.route('/funds/delete/<int:fund_id>', methods=['DELETE'])
def delete_fund_from_funds_db(fund_id):
    try:
        connection = get_db_connection(FUNDS_DB_FILE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM funds WHERE id = ?", (fund_id,))
        if cursor.rowcount == 0:
            return jsonify({"error": f"Fund with ID {fund_id} not found"}), 404

        connection.commit()
        connection.close()
        return jsonify({"message": f"Fund with ID {fund_id} deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": "Failed to delete fund from funds.db", "details": str(e)}), 500


# Main execution
if __name__ == '__main__':
    app.run(debug=True)
