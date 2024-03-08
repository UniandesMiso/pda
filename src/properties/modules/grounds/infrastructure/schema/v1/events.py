from pulsar.schema import Record, String, Float, Integer

from properties.seedwork.infrastructure.schema.v1.events import IntegrationEvent


class SaleRegisteredPayload(Record):
    sale_id = String()
    property_id = String()
    price = Float()
    currency = String()
    executed_at = Integer()


class SaleRegisteredEvent(IntegrationEvent):
    data = SaleRegisteredPayload()


class PropertyProcessedPayload(Record):
    property_id = String()
    width = Float()
    length = Float()


class PropertyProcessedEvent(IntegrationEvent):
    data = PropertyProcessedPayload()
