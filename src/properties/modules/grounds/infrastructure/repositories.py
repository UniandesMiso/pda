from uuid import UUID
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from properties.config.db import db
from properties.seedwork.infrastructure.utils import get_database_url
from properties.modules.grounds.domain.entities import Ground
from properties.modules.grounds.domain.repositories import GroundRepository
from properties.modules.grounds.infrastructure.mappers import GroundMapper
from properties.modules.grounds.infrastructure.dto import Ground as GroundDTO
from properties.seedwork.domain.entities import Entity


class GroundRepositorySQL(GroundRepository):

    def create(self, entity: Entity):
        entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        mapper = GroundMapper()
        ground_dto = mapper.entity_2_dto(entity)
        db.session.add(ground_dto)

    def update(self, entity: Ground):
        engine = create_engine(get_database_url())
        with Session(engine) as session:
            update = {"updated_at": datetime.now()}
            if (entity.dimension.width): update.update(width=entity.dimension.width)
            if (entity.dimension.length): update.update(length=entity.dimension.length)
            if (entity.amount.price): update.update(price=entity.amount.price)
            if (entity.amount.currency): update.update(currency=entity.amount.currency)
            session.query(GroundDTO).filter(GroundDTO.id == str(entity.id)).update(update)
            session.commit()
            session.close()

    def get_by_id(self, id: UUID) -> Ground:
        ground_dto = db.session.query(GroundDTO).get(id)
        mapper = GroundMapper()
        ground = mapper.dto_2_entity(ground_dto)
        return ground
