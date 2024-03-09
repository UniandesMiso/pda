from uuid import UUID
from dataclasses import dataclass

from contracts.seedwork.domain.events import DomainEvent


class GroundEvent(DomainEvent): ...


@dataclass
class AmountUpdated(GroundEvent):
    property_id: UUID
    sale_id: str
    price: float
    currency: str


@dataclass
class AmountUpdateFailed(GroundEvent):
    property_id: UUID
    sale_id: str
    price: float
    currency: str
