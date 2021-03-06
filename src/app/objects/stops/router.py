from typing import List, Any
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session

from database.session import get_db

from objects.stops.schemas import Stops
from objects.stops import crud

stops = APIRouter()

@stops.get("/", response_model=List[Stops])
def get_multiple_stops(db: Session = Depends(get_db), skip: int = 0, limit: int = 10,) -> List[Stops]:
    """
    Buscar todas as Stops.
    """
    stops = crud.stops.get_multi(db, skip=skip, limit=limit)
    
    return stops

@stops.get("/{stop_substring}", response_model=List[Stops])
def get_stops_substr(*, db: Session = Depends(get_db), stop_substring: str) -> List[Stops]:
    """
    Busca por pontos de paradas (stops) por meio de uma substring de entrada.
    """
    stops = crud.stops.get_stops_substr(db, substr = stop_substring)
    
    return stops

@stops.get("/by_trip/{trip_id}", response_model=List[Stops])
def get_multiple_stops_by_trip(*, db: Session = Depends(get_db), trip_id: str, limit: int = 10) -> List[Stops]:
    """
    Busca pelos pontos de parada (stops) que compõem um determinado trajeto (trip) por meio do ID do trajeto. 
    """
    stops = crud.stops.get_multi_by_trip(db, trip_id = trip_id, limit=limit)
    
    return stops

@stops.get("/{lat_0}/{lng_0}/{lat_1}/{lng_1}", response_model=List[Stops])
def get_multiple_stops_by_area(*, db: Session = Depends(get_db), lat_0: float, lng_0: float, lat_1: float, lng_1: float, limit: int = 100) -> List[Stops]:
    """
    Busca por pontos de paradas (stops) cujas localizações geográficas estiverem dentro da região informada.  
    """
    stops = crud.stops.get_multi_by_area(db, data_0 = (lat_0, lng_0), data_1 = (lat_1, lng_1), limit=limit)
    
    return stops

@stops.get("/id/{stop_id}", response_model=Stops)
def get_stop(*, db: Session = Depends(get_db), stop_id: int) -> Stops:
    """
    Buscar a Stop especificada.
    """
    stop = crud.stops.get_stop(db, id=stop_id)
    
    return stop