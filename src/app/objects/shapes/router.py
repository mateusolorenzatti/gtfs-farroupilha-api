from typing import List, Any
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session

from database.session import get_db

from objects.shapes.schemas import Shapes
from objects.shapes import crud

shapes = APIRouter()

@shapes.get("/", response_model=List[Shapes])
def get_multiple_shapes(db: Session = Depends(get_db), skip: int = 0, limit: int = 10,) -> List[Shapes]:
    """
    Buscar todas as Shapes.
    """
    shapes = crud.shapes.get_multi(db, skip=skip, limit=limit)
    
    return shapes

@shapes.get("/by_trip/{trip_id}", response_model=List[Shapes])
def get_shape(*, db: Session = Depends(get_db), trip_id: str,) -> List[Shapes]:
    """
    Busca pelos pontos que formam o desenho de um determinado trajeto (trip) por meio do ID do trajeto. 
    """
    shape = crud.shapes.get_multiple_shapes_by_trip(db, trip_id = trip_id)
    
    return shape

@shapes.get("/id/{shape_id}", response_model=Shapes)
def get_shape(*, db: Session = Depends(get_db), shape_id: str) -> Shapes:
    """
    Buscar a Shape especificada.
    """
    shape = crud.shapes.get_shape(db, id=shape_id)
    
    return shape