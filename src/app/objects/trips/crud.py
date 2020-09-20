from typing import List, Any, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from core.crud import CRUDBase

from .model import Trips
from .schemas import TripsCreate, TripsUpdate

class CRUDTrips(CRUDBase[Trips, TripsCreate, TripsUpdate]):
    
    def get_trip(self, db: Session, id: Any) -> Optional[Trips]:
        """Para manter a nomenclatura da tabela, foi criado a função que busca pelo trip_id. """

        return db.query(self.model).filter(self.model.trip_id == id).first()

trips = CRUDTrips(Trips)