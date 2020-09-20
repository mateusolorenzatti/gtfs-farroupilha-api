from typing import List, Any, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from core.crud import CRUDBase

from .model import Stops
from .schemas import StopsCreate, StopsUpdate

class CRUDStops(CRUDBase[Stops, StopsCreate, StopsUpdate]):
    
    def get_stop(self, db: Session, id: Any) -> Optional[Stops]:
        """Para manter a nomenclatura da tabela, foi criado a função que busca pelo stop_id. """

        return db.query(self.model).filter(self.model.stop_id == id).first()

stops = CRUDStops(Stops)