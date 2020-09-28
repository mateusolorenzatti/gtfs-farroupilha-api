import datetime

from typing import List, Any, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import cast, Time

from core.crud import CRUDBase

from .model import Trips
from .schemas import TripsCreate, TripsUpdate

# Tabelas para realizar Join
from objects.stop_times.model import StopTimes

class CRUDTrips(CRUDBase[Trips, TripsCreate, TripsUpdate]):
    
    def get_trip(self, db: Session, id: Any) -> Optional[Trips]:
        """Para manter a nomenclatura da tabela, foi criado a função que busca pelo trip_id. """

        return db.query(self.model).filter(self.model.trip_id == id).first()

    def get_multi_by_route(self, db: Session, route_id: int, limit: int = 100) -> List[Trips]:
        """ Filtrar através da rota informada """

        return db.query(self.model).filter(self.model.route_id == route_id).limit(limit).all()

    def get_multi_by_stop(self, db: Session, stop_id: int, limit: int = 100) -> List[Trips]:
        """ Filtrar através da parada informada """

        return db.query(self.model).join(StopTimes).filter(StopTimes.stop_id == stop_id).limit(limit).all()

    def get_multi_by_stop_and_time(self, db: Session, stop_id: int, start_time: str, end_time: str, limit: int = 100) -> List[Trips]:
        """ Filtrar através da parada informada dentro do período solicitado """

        date_pattern = '%H:%M:%S'

        start_time_date = datetime.datetime.strptime(start_time, date_pattern).time()
        end_time_date = datetime.datetime.strptime(end_time, date_pattern).time()

        arrival_time = StopTimes.arrival_time.cast(Time)

        return db.query(self.model).join(StopTimes).filter(StopTimes.stop_id == stop_id,arrival_time >= start_time_date, arrival_time <= end_time_date).order_by(arrival_time.asc()).limit(limit).all()

trips = CRUDTrips(Trips)