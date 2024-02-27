from properties.seedwork.application.dto import Mapper as ApplicationMapper
from properties.seedwork.domain.repositories import Mapper as RepositoryMapper
from properties.modules.grounds.application.dto import GroundDTO
from properties.modules.grounds.domain.entities import Ground


class GroundMapperDTO(ApplicationMapper):

    def dict_2_dto(self, dict: dict) -> GroundDTO:
        ground_dto = GroundDTO(
            id=dict.get("id"),
            address=dict.get("address"),
            status=dict.get("status"),
        )
        return ground_dto

    def dto_2_dict(self, dto: GroundDTO) -> dict:
        return dto.__dict__


class GroundMapper(RepositoryMapper):

    def get_type(self) -> type:
        return Ground.__class__

    def entity_2_dto(self, entity: Ground) -> GroundDTO:
        ground_dto = GroundDTO(
            id=entity.id,
            status=entity.status,
            address=entity.address,
        )
        return ground_dto

    def dto_2_entity(self, dto: GroundDTO) -> Ground:
        ground = Ground()
        ground.status = dto.status
        ground.address = dto.address
        return ground
