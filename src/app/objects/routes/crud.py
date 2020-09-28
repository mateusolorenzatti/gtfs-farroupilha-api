from typing import List, Any, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import func

from core.crud import CRUDBase

from .model import Routes
from .schemas import RoutesCreate, RoutesUpdate


class CRUDRoutes(CRUDBase[Routes, RoutesCreate, RoutesUpdate]):
    
    def get_route(self, db: Session, id: Any) -> Optional[Routes]:
        """Para manter a nomenclatura da tabela, foi criado a função que busca pelo route_id. """

        return db.query(self.model).filter(self.model.route_id == id).first()
    
    def get_route_substr(self, db: Session, substr: str, limit: int = 10) -> List[Routes]:
        """ Buscar por uma fração presente em nomes das rotas """

        return db.query(self.model).filter(func.lower(self.model.route_long_name).contains(func.lower(substr))).limit(limit).all()

routes = CRUDRoutes(Routes)