from typing import List, Any, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from core.crud import CRUDBase

from .model import StopTimes
from .schemas import StopTimesCreate, StopTimesUpdate

class CRUDStopTimes(CRUDBase[StopTimes, StopTimesCreate, StopTimesUpdate]):
    
    # def get_stop_time(self, db: Session, stop_sequence: Any) -> Optional[StopTimes]:
    #     """Para manter a nomenclatura da tabela, foi criado a função que busca pelo stop_sequence. """

    #     return db.query(self.model).filter(self.model.stop_sequence == stop_sequence).first()

    def get_multi_by_trip(self, db: Session, trip_id: str, limit: int = 100) -> List[StopTimes]:
        """ Filtrar através da trip informada """

        return db.query(self.model).filter(self.model.trip_id == trip_id).order_by(self.model.arrival_time.asc()).all()

stop_times = CRUDStopTimes(StopTimes)