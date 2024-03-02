from uuid import uuid4
from dataclasses import dataclass
from pydispatch import dispatcher
from typing import List

from listings.config.db import db
from listings.seedwork.application.commands import Command, CommandResult, execute_command as command
from listings.modules.listings.application.dto import ListingDTO, PropertyDTO
from listings.modules.listings.application.mappers import ListingMapper
from listings.modules.listings.application.commands.base import BaseCommandHandler

@dataclass
class ListingProperty:
    property_id: str
    width: str
    length: str

@dataclass
class ProcessListing(Command):
    properties: List[ListingProperty]
    executed_at: str

class ProcessListingHandler(BaseCommandHandler):

    def handle(self, command: ProcessListing) -> CommandResult:
        properties = []
        for property_data in command.properties:
            property_dto = PropertyDTO(
                id= property_data.id,
                propertyId= property_data.propertyId,
                width= property_data.width,
                length= property_data.length
            )
            properties.append(property_dto)

        listing_dto = ListingDTO(
            id=str(uuid4()),
            properties=properties,
            executedAt=command.executed_at,
        )

        mapper = ListingMapper()
        listing = mapper.dto_2_entity(listing_dto)
        listing.process_listing()

        for event in listing.events:
            dispatcher.send(event=event, signal=type(event).__name__)

        return CommandResult(data=mapper.entity_2_dto(listing))

@command.register(ProcessListing)
def execute_register_sale(command: ProcessListing):
    handler = ProcessListingHandler()
    return handler.handle(command)
