# Task 2: REST API Development Using Python and a web framework of your choice (e.g., Flask or Django)

Create a RESTful API to manage investment funds. The API should have the following endpoints
o Endpoint to retrieve a list of all funds
o Endpoint to create a new fund
o Endpoint to retrieve details of a specific fund using its ID
o Endpoint to update the performance of a fund using its ID
o Endpoint to delete a fund using its ID

# Investment Fund API
A RESTful API for managing investment funds using Flask. The 

## Features
- Retrieve all funds
- Create a new fund
- Retrieve a specific fund by ID
- Update the performance of a fund
- Delete a fund

## Requirements
- Python 3
- Flask

## How to Run
1. Clone the repository.
2. Install dependencies with `pip install -r test_requirements.txt`.
3. Run the application: `AHAM.py`.

## Endpoints
- `GET /funds`: Retrieve all funds.
- `POST /funds`: Create a new fund.
- `GET /funds/<fund_id>`: Retrieve a specific fund by ID.
- `PUT /funds/<fund_id>`: Update a fund's performance.
- `DELETE /funds/<fund_id>`: Delete a fund by ID.