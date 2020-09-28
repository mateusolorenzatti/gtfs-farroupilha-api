from typing import Optional

from pydantic import BaseModel

from objects.agency.schemas import Agency

# Shared properties
class RoutesBase(BaseModel):
    route_id: Optional[int]
    agency_id: Optional[int]
    route_short_name: Optional[str]
    route_long_name: Optional[str]
    route_desc: Optional[str]
    route_type: Optional[int]
    route_url: Optional[str]
    route_color: Optional[str]
    route_text_color: Optional[str]
    route_sort_order: Optional[int]
    min_headway_minutes: Optional[int]
    eligibility_restricted: Optional[int]

    # agency: Optional[Agency]

# Properties to receive on Routes creation
class RoutesCreate(RoutesBase):
    pass

# Properties to receive on Routes update
class RoutesUpdate(RoutesBase):
    pass

# Properties shared by models stored in DB
class RoutesInDBBase(RoutesBase):
    pass

    class Config:
        orm_mode = True

# Properties to return to client
class Routes(RoutesInDBBase):
    pass

# Properties properties stored in DB
class RoutesInDB(RoutesInDBBase):
    pass