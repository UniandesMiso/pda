from uuid import UUID
from datetime import datetime

from listings.config.db import db
from listings.modules.listings.domain.entities import Sale
from listings.modules.listings.domain.repositories import SaleRepository
from listings.modules.listings.domain.rules import PriceRequired
from listings.modules.listings.infrastructure.mappers import SaleMapper
from listings.modules.listings.infrastructure.dto import Sale as SaleDTO


class SaleRepositoryGeneric(SaleRepository):

    def create(self, entity: Sale):
        entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        entity.validate_rule(PriceRequired(entity))
        mapper = SaleMapper()
        sale_dto = mapper.entity_2_dto(entity)
        db.session.add(sale_dto)

    def get_by_id(self, id: UUID) -> Sale:
        sale_dto = db.session.query(SaleDTO).get(id)
        mapper = SaleMapper()
        sale = mapper.dto_2_entity(sale_dto)
        return sale
