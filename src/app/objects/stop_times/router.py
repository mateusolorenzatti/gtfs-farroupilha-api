from typing import List, Any
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session

from database.session import get_db

from objects.stop_times.schemas import StopTimes
from objects.stop_times import crud

stop_times = APIRouter()

@stop_times.get("/", response_model=List[StopTimes])
def get_multiple_stop_times(db: Session = Depends(get_db), skip: int = 0, limit: int = 10,) -> List[StopTimes]:
    """
    Buscar todas as StopTimes.
    """
    stop_times = crud.stop_times.get_multi(db, skip=skip, limit=limit)
    
    return stop_times

@stop_times.get("/by_trip/{trip_id}", response_model=List[StopTimes])
def get_multiple_stop_times_by_trip(*, db: Session = Depends(get_db), trip_id: str) -> List[StopTimes]:
    """
    Busca pelos pontos de parada e seus horários que compõem um determinado trajeto (trip) por meio do ID do trajeto. 
    """
    stop_times = crud.stop_times.get_multi_by_trip(db, trip_id = trip_id)
    
    return stop_times