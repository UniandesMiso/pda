from uuid import UUID
from datetime import datetime

from listings.seedwork.application.dto import Mapper as ApplicationMapper
from listings.seedwork.domain.repositories import Mapper as RepositoryMapper
from listings.seedwork.domain.entities import Amount
from listings.modules.information.application.dto import ListingDTO, PropertyDTO
from listings.modules.information.domain.entities import Listing


class ListingMapperDTO(ApplicationMapper):

    def dict_2_dto(self, dict: dict) -> ListingDTO:
        properties_data = dict.get("properties", [])
        property_dtos = []

        for property_data in properties_data:
            property_dto = PropertyDTO(
                id=property_data.get("id"),
                propertyId=property_data.get("propertyId"),
                width=property_data.get("width"),
                length=property_data.get("length"),
            )
            property_dtos.append(property_dto)

        listing_dto = ListingDTO(
            id=dict.get("id"),
            properties=property_dtos,
            createdAt=dict.get("createdAt"),
            updatedAt=dict.get("updatedAt"),
            executedAt=dict.get("executedAt"),
        )
        return listing_dto

    def dto_2_dict(self, dto: ListingDTO) -> dict:
        return dto.__dict__

class ListingMapper(RepositoryMapper):

    def get_type(self) -> type:
        return Listing.__class__

    def entity_2_dto(self, entity: Listing) -> ListingDTO:
        sale_dto = ListingDTO(
            id=entity.id,
            propertyId=entity.property_id,
            createdAt=entity.created_at.strftime("%d/%m/%Y %I:%M %p"),
            updatedAt=entity.updated_at.strftime("%d/%m/%Y %I:%M %p"),
            price=entity.amount.price,
            currency=entity.amount.currency,
            executedAt=entity.executed_at.strftime("%d/%m/%Y"),
        )
        return sale_dto

    def dto_2_entity(self, dto: ListingDTO) -> Listing:
        listing = Listing()
        listing.id = UUID(dto.id)
        listing.property_id = dto.propertyId
        listing.amount = Amount(price=dto.price, currency=dto.currency)
        listing.executed_at = datetime.strptime(dto.executedAt, "%d/%m/%Y")
        return listing
