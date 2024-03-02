from uuid import UUID
from datetime import datetime
from dataclasses import dataclass, field
from typing import List

from listings.seedwork.domain.events import DomainEvent

@dataclass(frozen=True)
class PropertyDTO():
    id: str = field(default_factory=str)
    propertyId: str = field(default_factory=str)
    width: str = field(default_factory=str)
    length: str = field(default_factory=str)

@dataclass
class PropertyProcessed(DomainEvent):

    def get_type(self):
        return PropertyProcessed.__class__

    propertyId: str = field(default_factory=UUID)
    width: str = field(default_factory=str)
    length: str = field(default_factory=str)
    executed_at: datetime = field(default_factory=datetime)

@dataclass
class ListingProcessed(DomainEvent):

    def get_type(self):
        return ListingProcessed.__class__

    properties: List[PropertyDTO] = field(default_factory=list)
    listing_id: UUID = field(default_factory=UUID)
    executed_at: datetime = field(default_factory=datetime)
