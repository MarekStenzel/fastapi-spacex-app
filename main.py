from typing import Dict

from fastapi import FastAPI, HTTPException
from cachetools import TTLCache

from apiservice import get_spacex_launch_info, get_spacex_rocket_info, get_spacex_crew_info_table
from timeservice import get_time_in_space_from_crew_member, get_warsaw_time
from models import FlightResponse, FlightRequest

app = FastAPI()

cache = TTLCache(maxsize=100, ttl=900)

@app.post('/flights', response_model=FlightResponse)
def get_flight_info(request_body: FlightRequest) -> Dict:

    cache_key = str(request_body)
    cached_data = cache.get(cache_key)
    if cached_data:
        print("Data retrieved from cache.")
        return cached_data

    flight_id = request_body.flightId

    if not flight_id:
        raise HTTPException(status_code=400, detail="Missing flightId in request body")

    spacex_launch_info = get_spacex_launch_info(flight_id)

    if spacex_launch_info is None:
        raise HTTPException(status_code=404,
                            detail=f"SpaceX launch info not found for flight ID: {flight_id}")

    crew_ids_list = spacex_launch_info['crew']

    crew_list = get_spacex_crew_info_table(crew_ids_list)

    if crew_list is None:
        raise HTTPException(status_code=404,
                            detail=f"SpaceX crew info not found for crew IDs List: {crew_ids_list}")

    crew = []
    for crew_member in crew_list:

        crew_selected_info = {
            "status": crew_member['status'],
            "name": crew_member['name'],
            "agency": crew_member['agency'],
            "number_of_flights": len(crew_member['launches']),
            "time_in_space": get_time_in_space_from_crew_member(crew_member['wikipedia'])
        }

        crew.append(crew_selected_info)

    rocket_id = spacex_launch_info['rocket']
    rocket_info = get_spacex_rocket_info(rocket_id)

    if rocket_info is None:
        raise HTTPException(status_code=404,
                            detail=f"SpaceX rocket info not found for rocket ID: {rocket_id}")

    data = {
        "is_success": spacex_launch_info['success'],
        "date": get_warsaw_time(spacex_launch_info['date_unix']),
        "name": spacex_launch_info['name'],
        "crew": crew,
        "rocket": {
            "rocket_name": rocket_info['name'],
            "first_flight": rocket_info['first_flight'],
            "company": rocket_info['company']
        }
    }

    cache[cache_key] = {'flight_id': flight_id, 'data': data}

    return {'flight_id': flight_id, 'data': data}
