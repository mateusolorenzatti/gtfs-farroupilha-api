from typing import List, Any, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from core.crud import CRUDBase

from .model import Shapes
from .schemas import ShapesCreate, ShapesUpdate

from objects.trips.model import Trips

class CRUDShapes(CRUDBase[Shapes, ShapesCreate, ShapesUpdate]):
    
    def get_shape(self, db: Session, id: Any) -> Optional[Shapes]:
        """Para manter a nomenclatura da tabela, foi criado a função que busca pelo shape_id. """

        return db.query(self.model).filter(self.model.shape_id == id).first()

    def get_multiple_shapes_by_trip(self, db: Session, *, trip_id: str) -> List[Shapes]:
        """ Filtrar os shapes pelo trip informado """

        return db.query(self.model).join(Trips, Trips.shape_id == self.model.shape_id).filter(Trips.trip_id == trip_id).order_by(self.model.shape_pt_sequence.asc()).all()

shapes = CRUDShapes(Shapes)