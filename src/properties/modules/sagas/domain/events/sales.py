from uuid import UUID
from datetime import datetime
from dataclasses import dataclass

from properties.seedwork.domain.events import DomainEvent


class SalesEvent(DomainEvent): ...


@dataclass
class SaleRegistered(SalesEvent):
    sale_id: UUID
    property_id: str
    price: float
    currency: str
    executed_at: datetime


@dataclass
class SaleRegisterFailed(SalesEvent):
    sale_id: UUID
    property_id: str
    price: float
    currency: str
    executed_at: datetime
