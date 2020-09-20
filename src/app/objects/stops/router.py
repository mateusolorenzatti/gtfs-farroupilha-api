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

@stops.get("/{stop_id}", response_model=Stops)
def get_stop(*, db: Session = Depends(get_db), stop_id: int) -> Stops:
    """
    Buscar a Stop especificada.
    """
    stop = crud.stops.get_stop(db, id=stop_id)
    
    return stop