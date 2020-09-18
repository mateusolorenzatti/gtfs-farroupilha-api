from typing import List, Any
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session

from database.session import get_db

from objects.agency.schemas import Agency
from objects.agency import crud

router = APIRouter()

@router.get("/", response_model=List[Agency])
def get_multiple_agencies(db: Session = Depends(get_db), skip: int = 0, limit: int = 10,) -> List[Agency]:
    """
    Buscar todas as Agencias.
    """
    agencies = crud.agency.get_multi(db, skip=skip, limit=limit)
    
    return agencies

@router.get("/{id}", response_model=Agency)
def get_agency(*, db: Session = Depends(get_db), id: int) -> Agency:
    """
    Buscar a Agencia especificada.
    """
    agency = crud.agency.get_agency(db, id=id)
    
    return agency