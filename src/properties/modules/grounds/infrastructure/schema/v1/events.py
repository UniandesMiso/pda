from pulsar.schema import Record, String, Float

from properties.seedwork.infrastructure.schema.v1.events import IntegrationEvent


class AmountUpdatedPayload(Record):
    ground_id = String()
    price = Float()
    currency = String()


class AmountUpdatedEvent(IntegrationEvent):
    data = AmountUpdatedPayload()
