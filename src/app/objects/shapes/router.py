from typing import List, Any
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session

from database.session import get_db

from objects.shapes.schemas import Shapes
from objects.shapes import crud

router = APIRouter()

@router.get("/", response_model=List[Shapes])
def get_multiple_agencies(db: Session = Depends(get_db), skip: int = 0, limit: int = 10,) -> List[Shapes]:
    """
    Buscar todas as Agencias.
    """
    shapes = crud.shapes.get_multi(db, skip=skip, limit=limit)
    
    return shapes

@router.get("/{id}", response_model=Shapes)
def get_shape(*, db: Session = Depends(get_db), id: str) -> Shapes:
    """
    Buscar a Agencia especificada.
    """
    shape = crud.shapes.get_shape(db, id=id)
    
    return shape