from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Float, PrimaryKeyConstraint

from core.base_class import Base

class Shapes(Base):
    shape_id_serial = Column(Integer, primary_key=True, index=True)
    shape_id = Column(String, primary_key=True, index=True)
    shape_pt_lat = Column(Float)
    shape_pt_lon = Column(Float)
    shape_pt_sequence = Column(Integer)
    shape_dist_traveled = Column(Float)
