from typing import Optional
from datetime import datetime, timezone
from bs4 import BeautifulSoup

import requests
import pytz

def get_time_in_space_from_crew_member(url: str) -> Optional[str]:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            time_in_space_element = soup.find('th', string='Time in space')

            if time_in_space_element:
                return time_in_space_element.find_next('td').get_text(strip=True)

    except requests.exceptions.Timeout:
        print("Timeout error for Wikipedia")
        return None

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Request exception {e}")
        return None


def get_warsaw_time(unix_timestamp: int) -> str:
    utc_time = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc)
    warsaw_timezone = pytz.timezone('Europe/Warsaw')
    warsaw_time = utc_time.astimezone(warsaw_timezone).strftime('%Y-%m-%d %H:%M:%S')

    return str(warsaw_time)
