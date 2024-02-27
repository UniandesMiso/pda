from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from properties.seedwork.infrastructure.utils import get_database_url
from properties.modules.grounds.domain.entities import Ground
from properties.modules.grounds.domain.repositories import GroundRepository
from properties.modules.grounds.infrastructure.mappers import GroundMapper


class GroundRepositoryGeneric(GroundRepository):

    def update(self, entity: Ground):
        try:
            engine = create_engine(get_database_url())
            with Session(engine) as session:
                mapper = GroundMapper()
                ground_dto = mapper.entity_2_dto(entity)
                session.add(ground_dto)
                session.commit()
        except Exception as ex:
            print(str(ex))
