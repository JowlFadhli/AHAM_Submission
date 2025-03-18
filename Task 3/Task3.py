import sqlite3
import os

# Database file name
DB_FILE = 'funds.db'

# Establish connection to the database
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Ensure the database schema is created
# Create the funds table if it doesn't already exist
def initialize_database():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS funds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fund_name TEXT NOT NULL UNIQUE,
        performance REAL NOT NULL
    )
    """)
    connection.commit()

# Add a new fund to the SQLite database
def create_fund(fund_name, performance):
    try:
        cursor.execute("INSERT INTO funds (fund_name, performance) VALUES (?, ?)", (fund_name, performance))
        connection.commit()
        print(f"Fund '{fund_name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: A fund with the name '{fund_name}' already exists.")

# Update the performance of an existing fund
def update_fund(fund_name, new_performance):
    cursor.execute("UPDATE funds SET performance = ? WHERE fund_name = ?", (new_performance, fund_name))
    if cursor.rowcount > 0:
        connection.commit()
        print(f"Fund '{fund_name}' updated successfully.")
    else:
        print(f"Error: Fund '{fund_name}' not found.")

# List all funds in the SQLite database
def list_funds():
    cursor.execute("SELECT * FROM funds")
    funds = cursor.fetchall()
    if funds:
        print("Available Funds:")
        for fund in funds:
            print(f"ID: {fund[0]}, Name: {fund[1]}, Performance: {fund[2]:.2f}%")
    else:
        print("No funds available.")


# Close the database connection properly
def close_connection():
    connection.close()
    print("Database connection closed.")


# Code testing and validation
if __name__ == "__main__":
    initialize_database()

    while True:
        print("\nMenu:")
        print("1. New fund creation")
        print("2. Update Fund's Perfromance")
        print("3. Fund list")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            fund_name = input("Enter fund name: ")
            performance = float(input("Enter fund performance (%): "))
            create_fund(fund_name, performance)
        elif choice == '2':
            fund_name = input("Enter fund name to update: ")
            new_performance = float(input("Enter new performance (%): "))
            update_fund(fund_name, new_performance)
        elif choice == '3':
            list_funds()
        elif choice == '4':
            close_connection()
            break
        else:
            print("Invalid option. Please try again.")
