from typing import List, Any, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from core.crud import CRUDBase

from .model import Agency
from .schemas import AgencyCreate, AgencyUpdate

class CRUDAgency(CRUDBase[Agency, AgencyCreate, AgencyUpdate]):
    
    def get_agency(self, db: Session, id: Any) -> Optional[Agency]:
        """Para manter a nomenclatura da tabela, foi criado a função que busca pelo agency_id. """

        return db.query(self.model).filter(self.model.agency_id == id).first()

agency = CRUDAgency(Agency)