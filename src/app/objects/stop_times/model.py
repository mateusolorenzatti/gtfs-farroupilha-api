from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Float, PrimaryKeyConstraint, ForeignKey

from core.base_class import Base

class StopTimes(Base):  
    __tablename__ = 'stop_times'
    
    arrival_time = Column(String)
    departure_time = Column(String)
    stop_sequence = Column(Integer, primary_key=True, index=True)
    stop_headsign = Column(String)
    pickup_type = Column(Integer)
    drop_off_type = Column(Integer)
    shape_dist_traveled = Column(Float)
    timepoint = Column(Integer)
    start_service_area_id = Column(String)
    end_service_area_id = Column(String)
    start_service_area_radius = Column(String)
    end_service_area_radius = Column(String)
    continuous_pickup = Column(String)
    continuous_drop_off = Column(String)
    pickup_area_id = Column(String)
    drop_off_area_id = Column(String)
    pickup_service_area_radius = Column(String)
    drop_off_service_area_radius = Column(String)

    stop_id = Column(Integer, ForeignKey("stops.stop_id"), index=True)
    trip_id = Column(String, ForeignKey("trips.trip_id"), index=True)