from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint

from core.base_class import Base

class Agency(Base):
    agency_id = Column(Integer, primary_key=True, index=True)
    agency_url = Column(String)
    agency_lang = Column(String)
    agency_name = Column(String)
    agency_phone = Column(String)
    agency_timezone = Column(String)
    agency_fare_url = Column(String)
    