from uuid import UUID
from datetime import datetime
from dataclasses import dataclass, field

from contracts.seedwork.domain.events import DomainEvent


@dataclass
class SaleRegistered(DomainEvent):
    sale_id: UUID = field(default_factory=UUID)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
    executed_at: datetime = field(default_factory=datetime)
