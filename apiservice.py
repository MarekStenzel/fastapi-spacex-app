from typing import List, Optional
from models import SpaceXLaunchInfo, SpaceXCrewInfo, SpaceXRocketInfo

import requests

def get_spacex_crew_info_table(crew_ids_list: List[str]) -> Optional[List[SpaceXCrewInfo]]:
    url = "https://api.spacexdata.com/v4/crew/query"

    query_payload = {
        "query": {
            "_id": crew_ids_list
        }
    }

    try:
        response = requests.post(url, json=query_payload, timeout=5)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            return data['docs']

    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")
        return None

def get_spacex_launch_info(flight_id: str) -> Optional[SpaceXLaunchInfo]:
    url = "https://api.spacexdata.com/v4/launches/query"

    query_payload = {
        "query": {
            "_id": flight_id
        },
        "options": {
            "populate": [
                "rocket"
            ]
        }
    }

    try:
        response = requests.post(url, json=query_payload, timeout=5)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            return data['docs'][0]

    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")
        return None
