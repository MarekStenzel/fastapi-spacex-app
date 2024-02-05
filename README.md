# FastAPI SpaceX Flight Information App

This FastAPI application provides information about SpaceX flights, including details about launches, crew members, and rockets.

## Requirements

- Python 3.9+
- Docker

## Installation

Clone the repository:

`git clone https://github.com/MarekStenzel/fastapi-spacex-app.git`

Change directory to the project folder:

`cd fastapi-spacex-app`

Install the required dependencies using Poetry:

`poetry install`

## Usage

Run the FastAPI application using Poetry:

`poetry run uvicorn main:app --reload`

## Docker

To run the application using Docker Compose:

`docker compose build && docker compose up`

## Endpoints

`/flights` - get flights information

Method: **POST**

Path: `/flights`

Example:

Request Body:
```
{
    "flightId": "62dd70d5202306255024d139"
}
```
Response:
```
{
    "flight_id": "62dd70d5202306255024d139",
    "data": {
        "is_success": true,
        "date": "2022-10-05 18:00:00",
        "name": "Crew-5",
        "crew": [
            {
                "status": "active",
                "name": "Nicole Aunapu Mann",
                "agency": "NASA",
                "number_of_flights": 1,
                "time_in_space": "157d 10h 1m"
            },
            {
                "status": "active",
                "name": "Josh A. Cassada",
                "agency": "NASA",
                "number_of_flights": 1,
                "time_in_space": "157d 10h 1m"
            },
            {
                "status": "active",
                "name": "Koichi Wakata",
                "agency": "JAXA",
                "number_of_flights": 1,
                "time_in_space": "504 days, 18 hours and 33 minutes"
            },
            {
                "status": "active",
                "name": "Anna Kikina",
                "agency": "Roscosmos",
                "number_of_flights": 1,
                "time_in_space": "157 days, 10 hours and 1 minute"
            }
        ],
        "rocket": {
            "rocket_name": "Falcon 9",
            "first_flight": "2010-06-04",
            "company": "SpaceX"
        }
    }
}
```