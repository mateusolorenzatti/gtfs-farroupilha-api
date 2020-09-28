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

@trips.get("/by_route/{route_id}", response_model=List[Trips])
def get_multiple_trips_by_route(*, db: Session = Depends(get_db), route_id: int, limit: int = 10) -> List[Trips]:
    """
    Busca por trajetos (trips) por meio do ID de uma rota. 
    """
    trips = crud.trips.get_multi_by_route(db, route_id = route_id, limit=limit)
    
    return trips

@trips.get("/by_stop/{stop_id}", response_model=List[Trips])
def get_multiple_trips_by_stop(*, db: Session = Depends(get_db), stop_id: int, limit: int = 10) -> List[Trips]:
    """
    Busca por trajetos (trips) por meio do ID de uma das paradas que está contida neste trajeto. 
    """
    trips = crud.trips.get_multi_by_stop(db, stop_id = stop_id, limit=limit)
    
    return trips

@trips.get("/by_stop/{stop_id}/{start_time}/{end_time}", response_model=List[Trips])
def get_multiple_trips_by_stop_and_time(*, db: Session = Depends(get_db), stop_id: int, start_time: str, end_time: str, limit: int = 10) -> List[Trips]:
    """
    Busca por trajetos (trips) por meio do ID de uma das paradas que está contida neste trajeto, filtrando apenas aqueles trajetos que passam por esta parada dentro de um intervalo de tempo recebido por parâmetro.
    """
    trips = crud.trips.get_multi_by_stop_and_time(db, stop_id = stop_id, start_time = start_time, end_time = end_time, limit=limit)
    
    return trips

@trips.get("/id/{trip_id}", response_model=Trips)
def get_trip(*, db: Session = Depends(get_db), trip_id: str) -> Trips:
    """
    Buscar a Trip especificada.
    """
    trip = crud.trips.get_trip(db, id=trip_id)
    
    return trip