from dataclasses import dataclass, field
from typing import List

from listings.seedwork.application.dto import DTO

@dataclass(frozen=True)
class PropertyDTO(DTO):
    id: str = field(default_factory=str)
    propertyId: str = field(default_factory=str)
    width: str = field(default_factory=str)
    length: str = field(default_factory=str)

@dataclass(frozen=True)
class ListingDTO(DTO):
    id: str = field(default_factory=str)
    properties: List[PropertyDTO] = field(default_factory=list)
    createdAt: str = field(default_factory=str)
    updatedAt: str = field(default_factory=str)
    executedAt: str = field(default_factory=str)
