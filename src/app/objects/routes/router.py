from typing import List, Any
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session

from database.session import get_db

from objects.routes.schemas import Routes
from objects.routes import crud

router = APIRouter()

@router.get("/", response_model=List[Routes])
def get_multiple_routes(db: Session = Depends(get_db), skip: int = 0, limit: int = 10,) -> List[Routes]:
    """
    Buscar todas as Rotas.
    """
    routes = crud.routes.get_multi(db, skip=skip, limit=limit)
    
    return routes

@router.get("/{id}", response_model=Routes)
def get_route(*, db: Session = Depends(get_db), id: int) -> Routes:
    """
    Buscar a Rota especificada.
    """
    route = crud.routes.get_route(db, id=id)
    
    return route