from typing import List, Any, Optional
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session

from database.session import get_db

from objects.routes.schemas import Routes
from objects.routes import crud

routes = APIRouter()

@routes.get("/", response_model=List[Routes])
def get_multiple_routes(db: Session = Depends(get_db), skip: int = 0, limit: int = 10,) -> List[Routes]:
    """
    Buscar todas as Rotas.
    """
    routes = crud.routes.get_multi(db, skip=skip, limit=limit)
    
    return routes

@routes.get("/{route_substring}", response_model=List[Routes])
def get_route_substr(*, db: Session = Depends(get_db), route_substring: str) -> Routes:
    """
    Busca por rotas (route) por meio de uma substring de entrada. 
    """
    routes = crud.routes.get_route_substr(db, substr = route_substring)
    
    return routes

@routes.get("/id/{route_id}", response_model=Routes)
def get_route(*, db: Session = Depends(get_db), route_id: int) -> Routes:
    """
    Buscar a Rota especificada.
    """
    route = crud.routes.get_route(db, id=route_id)
    
    return route
