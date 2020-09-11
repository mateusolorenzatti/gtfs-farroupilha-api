from typing import List, Any, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from core.crud import CRUDBase

from .model import Routes
from .schemas import RoutesCreate, RoutesUpdate


class CRUDRoutes(CRUDBase[Routes, RoutesCreate, RoutesUpdate]):
    
    def get_route(self, db: Session, id: Any) -> Optional[Routes]:
        """Para manter a nomenclatura da tabela, foi criado a função que busca pelo route_id. """

        return db.query(self.model).filter(self.model.route_id == id).first()

    # def get_multi_by_owner(
    #     self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    # ) -> List[Item]:
    #     return (
    #         db.query(self.model)
    #         .filter(Item.owner_id == owner_id)
    #         .offset(skip)
    #         .limit(limit)
    #         .all()
    #     )

routes = CRUDRoutes(Routes)