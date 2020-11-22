from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Float, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.orm import relationship

from core.base_class import Base
from objects.shapes.model import Shapes

class Trips(Base):

    trip_id = Column(String, primary_key=True)
    service_id = Column(String, index=True)
    trip_short_name = Column(String)
    trip_headsign = Column(String)
    direction_id = Column(Integer, index=True)
    block_id = Column(Integer)
    bikes_allowed = Column(Integer)
    wheelchair_accessible = Column(Integer)
    trip_type = Column(Integer)
    drt_max_travel_time = Column(Integer)
    drt_avg_travel_time = Column(Integer)
    drt_advance_book_min = Column(Integer)
    drt_pickup_message = Column(Integer)
    drt_drop_off_message = Column(Integer)
    continuous_pickup_message = Column(String)
    continuous_drop_off_message = Column(String)

    # FKs
    route_id = Column(Integer, ForeignKey("routes.route_id"), index=True)
    route = relationship("Routes", foreign_keys=[route_id])

    shape_id = Column(String, ForeignKey("shapes.shape_id"), index=True)
    # shape_id_serial = Column(Integer, ForeignKey("shapes.shape_id_serial"))

    shape = relationship("Shapes", foreign_keys=[shape_id], order_by=Shapes.shape_pt_sequence)