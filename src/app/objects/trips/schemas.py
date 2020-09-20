
from typing import Optional

from pydantic import BaseModel

# Shared properties
class TripsBase(BaseModel):

    trip_id: Optional[str]
    service_id: Optional[str]
    trip_short_name: Optional[str]
    trip_headsign: Optional[str]
    direction_id: Optional[int]
    block_id: Optional[int]
    bikes_allowed: Optional[int]
    wheelchair_accessible: Optional[int]
    trip_type: Optional[int]
    drt_max_travel_time: Optional[int]
    drt_avg_travel_time: Optional[int]
    drt_advance_book_min: Optional[int]
    drt_pickup_message: Optional[int]
    drt_drop_off_message: Optional[int]
    continuous_pickup_message: Optional[str]
    continuous_drop_off_message: Optional[str]

    route_id: Optional[int]
    shape_id: Optional[str]
    shape_id_serial: Optional[int]

# Properties to receive on Routes creation
class TripsCreate(TripsBase):
    pass

# Properties to receive on Routes update
class TripsUpdate(TripsBase):
    pass

# Properties shared by models stored in DB
class TripsInDBBase(TripsBase):
    pass

    class Config:
        orm_mode = True

# Properties to return to client
class Trips(TripsInDBBase):
    pass

# Properties properties stored in DB
class TripsInDB(TripsInDBBase):
    pass
