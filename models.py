from typing import List, Optional
from pydantic import BaseModel, UUID1

class Failure(BaseModel):
    time: Optional[float]
    altitude: Optional[float]
    reason: Optional[str]

class Core(BaseModel):
    core: Optional[UUID1]
    flight: Optional[float]
    gridfins: Optional[bool]
    legs: Optional[bool]
    reused: Optional[bool]
    landing_attempt: Optional[bool]
    landing_success: Optional[bool]
    landing_type: Optional[str]
    landpad: Optional[UUID1]

class Fairings(BaseModel):
    reused: Optional[bool]
    recovery_attempt: Optional[bool]
    recovered: Optional[bool]
    ships: Optional[List[UUID1]]

class Links(BaseModel):
    patch: Optional[dict]
    reddit: Optional[dict]
    flickr: Optional[dict]
    presskit: Optional[str]
    webcast: Optional[str]
    youtube_id: Optional[str]
    article: Optional[str]
    wikipedia: Optional[str]

class SpaceXLaunchInfo(BaseModel):
    flight_number: int
    name: str
    date_utc: str
    date_unix: float
    date_local: str
    date_precision: str
    static_fire_date_utc: Optional[str]
    static_fire_date_unix: Optional[float]
    tdb: Optional[bool]
    net: Optional[bool]
    window: Optional[float]
    rocket: Optional[UUID1]
    success: Optional[bool]
    failures: Optional[List[Failure]]
    upcoming: bool
    details: Optional[str]
    fairings: Optional[Fairings]
    crew: Optional[List[UUID1]]
    ships: Optional[List[UUID1]]
    capsules: Optional[List[UUID1]]
    payloads: Optional[List[UUID1]]
    launchpad: Optional[UUID1]
    cores: Optional[List[Core]]
    links: Optional[Links]
    auto_update: Optional[bool]

class SpaceXCrewInfo(BaseModel):
    name: Optional[str] = None
    status: str
    agency: Optional[str] = None
    image: Optional[str] = None
    wikipedia: Optional[str] = None
    launches: Optional[List[UUID1]] = []

class SpaceXRocketInfo(BaseModel):
    name: str
    type: str
    active: bool
    stages: int
    boosters: int
    cost_per_launch: float
    success_rate_pct: float
    first_flight: str
    country: str
    company: str
    height: dict
    diameter: dict
    mass: dict
    payload_weights: List[dict]
    first_stage: dict
    second_stage: dict
    engines: dict
    landing_legs: dict
    flickr_images: List[str]
    wikipedia: Optional[str] = None
    description: Optional[str] = None

class FlightRequest(BaseModel):
    flightId: str

class CrewMember(BaseModel):
    status: str
    name: str
    agency: str
    number_of_flights: int
    time_in_space: str

class Rocket(BaseModel):
    rocket_name: str
    first_flight: str
    company: str

class FlightResponseData(BaseModel):
    is_success: bool
    date: str
    name: str
    crew: List[CrewMember]
    rocket: Rocket

class FlightResponse(BaseModel):
    flight_id: str
    data: FlightResponseData
