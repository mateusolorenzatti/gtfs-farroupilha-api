from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.base_class import Base

class Routes(Base):
    route_id = Column(Integer, primary_key=True, index=True)
    route_short_name = Column(String)
    route_long_name = Column(String)
    route_desc = Column(String)
    route_type = Column(Integer)
    route_url = Column(String)
    route_color = Column(String)
    route_text_color = Column(String)
    route_sort_order = Column(Integer)
    min_headway_minutes = Column(Integer)
    eligibility_restricted = Column(Integer)

    agency_id = Column(Integer, ForeignKey("agency.agency_id"))
    # agency = relationship("Agency")