
from typing import Optional

from pydantic import BaseModel

# Shared properties
class StopTimesBase(BaseModel):

    arrival_time: Optional[str]
    departure_time: Optional[str]
    stop_sequence: Optional[int]
    stop_headsign: Optional[str]
    pickup_type: Optional[int]
    drop_off_type: Optional[int]
    shape_dist_traveled: Optional[float]
    timepoint: Optional[int]
    start_service_area_id: Optional[str]
    end_service_area_id: Optional[str]
    start_service_area_radius: Optional[str]
    end_service_area_radius: Optional[str]
    continuous_pickup: Optional[str]
    continuous_drop_off: Optional[str]
    pickup_area_id: Optional[str]
    drop_off_area_id: Optional[str]
    pickup_service_area_radius: Optional[str]
    drop_off_service_area_radius: Optional[str]

    stop_id: Optional[int]
    trip_id: Optional[str]


# Properties to receive on Routes creation
class StopTimesCreate(StopTimesBase):
    pass

# Properties to receive on Routes update
class StopTimesUpdate(StopTimesBase):
    pass

# Properties shared by models stored in DB
class StopTimesInDBBase(StopTimesBase):
    pass

    class Config:
        orm_mode = True

# Properties to return to client
class StopTimes(StopTimesInDBBase):
    pass

# Properties properties stored in DB
class StopTimesInDB(StopTimesInDBBase):
    pass
