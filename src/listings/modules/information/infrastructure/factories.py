from dataclasses import dataclass

from listings.seedwork.domain.events import DomainEvent
from listings.seedwork.domain.factories import Factory
from listings.seedwork.domain.exceptions import FactoryException
from listings.seedwork.infrastructure.schema.v1.events import IntegrationEvent
from listings.modules.information.domain.events import SaleRegistered
from listings.modules.information.infrastructure.schema.v1.events import SaleRegisteredPayload, SaleRegisteredEvent


@dataclass
class FactoryEvents(Factory):

    def create_object(self, event: DomainEvent) -> IntegrationEvent:
        if event.get_type() == SaleRegistered.__class__:
            payload = SaleRegisteredPayload(
                sale_id=str(event.id),
                property_id=event.property_id,
                price=event.price,
                currency=event.currency,
                executed_at=int(event.executed_at.timestamp()),
            )
            return SaleRegisteredEvent(data=payload)

        else:
            raise FactoryException("The factory does not exist for the requested type")
