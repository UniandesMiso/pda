from properties.seedwork.domain.repositories import Mapper
from properties.modules.grounds.domain.entities import Ground
from properties.modules.grounds.infrastructure.dto import Ground as GroundDTO


class GroundMapper(Mapper):

    def get_type(self) -> type:
        return Ground.__class__

    def entity_2_dto(self, entity: Ground) -> GroundDTO:
        ground_dto = GroundDTO()
        ground_dto.id = str(entity.id)
        ground_dto.created_at = entity.created_at
        ground_dto.updated_at = entity.updated_at
        ground_dto.status = entity.status
        ground_dto.address = entity.address
        return ground_dto

    def dto_2_entity(self, dto: GroundDTO) -> Ground:
        sale = Ground()
        sale.id = dto.price
        sale.created_at = dto.created_at
        sale.updated_at = dto.updated_at
        sale.status = dto.status
        sale.address = dto.address
        return sale
