from dataclasses import dataclass

from properties.seedwork.domain.events import DomainEvent
from properties.seedwork.domain.factories import Factory
from properties.seedwork.domain.exceptions import FactoryException
from properties.seedwork.infrastructure.schema.v1.events import IntegrationEvent
from properties.modules.grounds.domain.events import AmountUpdated
from properties.modules.grounds.infrastructure.schema.v1.events import AmountUpdatedPayload, AmountUpdatedEvent


@dataclass
class FactoryEvents(Factory):

    def create_object(self, event: DomainEvent) -> IntegrationEvent:
        if event.get_type() == AmountUpdated.__class__:
            payload = AmountUpdatedPayload(
                ground_id=str(event.ground_id),
                price=event.price,
                currency=event.currency,
            )
            return AmountUpdatedEvent(data=payload)
        else:
            raise FactoryException("The factory does not exist for the requested type")
