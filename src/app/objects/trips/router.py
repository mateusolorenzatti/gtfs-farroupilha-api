from typing import List, Any
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session

from database.session import get_db

from objects.trips.schemas import Trips
from objects.trips import crud

trips = APIRouter()

@trips.get("/", response_model=List[Trips])
def get_multiple_trips(db: Session = Depends(get_db), skip: int = 0, limit: int = 10,) -> List[Trips]:
    """
    Buscar todas as Trips.
    """
    trips = crud.trips.get_multi(db, skip=skip, limit=limit)
    
    return trips

@trips.get("/{trip_id}", response_model=Trips)
def get_trip(*, db: Session = Depends(get_db), trip_id: str) -> Trips:
    """
    Buscar a Trip especificada.
    """
    trip = crud.trips.get_trip(db, id=trip_id)
    
    return trip