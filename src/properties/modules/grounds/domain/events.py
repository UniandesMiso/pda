from uuid import UUID
from dataclasses import dataclass, field

from contracts.seedwork.domain.events import DomainEvent


@dataclass
class AmountUpdated(DomainEvent):

    def get_type(self):
        return AmountUpdated.__class__

    ground_id: UUID = field(default_factory=UUID)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)


@dataclass
class AmountUpdateFailed(DomainEvent):

    def get_type(self):
        return AmountUpdateFailed.__class__

    ground_id: UUID = field(default_factory=UUID)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
