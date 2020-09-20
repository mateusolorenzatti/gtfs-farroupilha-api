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

# @stop_times.get("/{id}", response_model=StopTimes)
# def get_stop_time(*, db: Session = Depends(get_db), stop_sequence: int) -> StopTimes:
#     """
#     Buscar a StopTime especificada.
#     """
#     stop_time = crud.stop_times.get_stop_time(db, id=id)
    
#     return stop_time