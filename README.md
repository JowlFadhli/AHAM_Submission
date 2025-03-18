# AFFIN HWANG ASSET MANAGEMENT Python Developer Assesment

# Investment Fund API
A RESTful API for managing investment funds using Flask and SQLite.

## Features
- Retrieve all funds
- Create a new fund
- Retrieve a specific fund by ID
- Update the performance of a fund
- Delete a fund

## Requirements
- Python 3.x
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