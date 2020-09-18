
from typing import Optional

from pydantic import BaseModel

# Shared properties
class AgencyBase(BaseModel):
  agency_id: Optional[int]
  agency_url: Optional[str]
  agency_lang: Optional[str]
  agency_name: Optional[str]
  agency_phone: Optional[str]
  agency_timezone: Optional[str]
  agency_fare_url: Optional[str]

# Properties to receive on Routes creation
class AgencyCreate(AgencyBase):
    pass

# Properties to receive on Routes update
class AgencyUpdate(AgencyBase):
    pass

# Properties shared by models stored in DB
class AgencyInDBBase(AgencyBase):
    pass

    class Config:
        orm_mode = True

# Properties to return to client
class Agency(AgencyInDBBase):
    pass

# Properties properties stored in DB
class AgencyInDB(AgencyInDBBase):
    pass
