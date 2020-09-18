
from typing import Optional

from pydantic import BaseModel

# Shared properties
class ShapesBase(BaseModel):
  shape_id_serial: Optional[int]
  shape_id: Optional[str]
  shape_pt_lat: Optional[float]
  shape_pt_lon: Optional[float]
  shape_pt_sequence: Optional[int]
  shape_dist_traveled: Optional[float]

# Properties to receive on Routes creation
class ShapesCreate(ShapesBase):
    pass

# Properties to receive on Routes update
class ShapesUpdate(ShapesBase):
    pass

# Properties shared by models stored in DB
class ShapesInDBBase(ShapesBase):
    pass

    class Config:
        orm_mode = True

# Properties to return to client
class Shapes(ShapesInDBBase):
    pass

# Properties properties stored in DB
class ShapesInDB(ShapesInDBBase):
    pass
