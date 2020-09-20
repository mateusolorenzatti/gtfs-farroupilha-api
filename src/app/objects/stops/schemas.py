
from typing import Optional

from pydantic import BaseModel

# Shared properties
class StopsBase(BaseModel):
    stop_id: Optional[int]
    stop_code: Optional[str]
    platform_code: Optional[str]
    stop_name: Optional[str]
    stop_desc: Optional[str]
    stop_lat: Optional[float]
    stop_lon: Optional[float]
    zone_id: Optional[int]
    stop_url: Optional[str]
    location_type: Optional[int]
    parent_station: Optional[int]
    stop_timezone: Optional[str]
    position: Optional[int]
    direction_id: Optional[int]
    wheelchair_boarding: Optional[int]

# Properties to receive on Routes creation
class StopsCreate(StopsBase):
    pass

# Properties to receive on Routes update
class StopsUpdate(StopsBase):
    pass

# Properties shared by models stored in DB
class StopsInDBBase(StopsBase):
    pass

    class Config:
        orm_mode = True

# Properties to return to client
class Stops(StopsInDBBase):
    pass

# Properties properties stored in DB
class StopsInDB(StopsInDBBase):
    pass
