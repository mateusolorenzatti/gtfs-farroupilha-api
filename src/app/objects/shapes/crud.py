from typing import List, Any, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from core.crud import CRUDBase

from .model import Shapes
from .schemas import ShapesCreate, ShapesUpdate

class CRUDShapes(CRUDBase[Shapes, ShapesCreate, ShapesUpdate]):
    
    def get_shape(self, db: Session, id: Any) -> Optional[Shapes]:
        """Para manter a nomenclatura da tabela, foi criado a função que busca pelo shape_id. """

        return db.query(self.model).filter(self.model.shape_id == id).first()

shapes = CRUDShapes(Shapes)