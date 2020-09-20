from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Float, PrimaryKeyConstraint

from core.base_class import Base

class Stops(Base):
    stop_id = Column(Integer, primary_key=True)
    stop_code = Column(String)
    platform_code = Column(String)
    stop_name = Column(String)
    stop_desc = Column(String)
    stop_lat = Column(Float, index=True)
    stop_lon = Column(Float, index=True)
    zone_id = Column(Integer)
    stop_url = Column(String)
    location_type = Column(Integer)
    parent_station = Column(Integer)
    stop_timezone = Column(String)
    position = Column(Integer)
    direction_id = Column(Integer)
    wheelchair_boarding = Column(Integer)