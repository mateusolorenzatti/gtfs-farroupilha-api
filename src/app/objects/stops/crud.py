from typing import List, Any, Optional, Tuple

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import func, and_

from core.crud import CRUDBase

from .model import Stops
from .schemas import StopsCreate, StopsUpdate

from objects.stop_times.model import StopTimes

class CRUDStops(CRUDBase[Stops, StopsCreate, StopsUpdate]):
    
    def get_stop(self, db: Session, id: Any) -> Optional[Stops]:
        """Para manter a nomenclatura da tabela, foi criado a função que busca pelo stop_id. """

        return db.query(self.model).filter(self.model.stop_id == id).first()

    def get_stops_substr(self, db: Session, substr: str, limit: int = 10) -> List[Stops]:
        """ Buscar por uma fração presente em nomes das stops """

        return db.query(self.model).filter(func.lower(self.model.stop_name).contains(func.lower(substr))).limit(limit).all()

    def get_multi_by_trip(self, db: Session, trip_id: str, limit: int = 100) -> List[Stops]:
        """ Filtrar através da trip informada """

        return db.query(self.model).join(StopTimes).filter(StopTimes.trip_id == trip_id).order_by(StopTimes.stop_sequence.asc()).limit(limit).all()
    
    def get_multi_by_area(self, db: Session, data_0: Tuple[float, float], data_1: Tuple[float, float], limit: int = 100) -> List[Stops]:
        """ Filtrar paradas dentro dos delimitadores informados """

        # print(" Ponto A: {}".format(data_0))
        # print(" Ponto B: {}".format(data_1))
 
        return db.query(self.model).filter(and_(self.model.stop_lat <= data_0[0], self.model.stop_lat >= data_1[0], self.model.stop_lon >= data_0[1], self.model.stop_lon <= data_1[1])).limit(limit).all()

stops = CRUDStops(Stops)