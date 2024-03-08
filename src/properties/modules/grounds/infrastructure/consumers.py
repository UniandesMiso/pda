from pulsar import Client
from pulsar.schema import AvroSchema
from pydispatch import dispatcher

from properties.seedwork.infrastructure.utils import get_pulsar_url
from properties.modules.grounds.infrastructure.schema.v1.events import SaleRegisteredEvent, PropertyProcessedEvent


def subscribe_2_sales_events():
    client = Client(get_pulsar_url())

    consumer = client.subscribe(
        topic="contracts-sales-events",
        subscription_name="contracts-sales-sub-properties",
        schema=AvroSchema(SaleRegisteredEvent),
    )

    while True:
        message = consumer.receive()
        try:
            consumer.acknowledge(message)
            event = message.value()
            dispatcher.send(event=event, signal=type(event).__name__)
        except:
            consumer.negative_acknowledge(message)


def subscribe_2_information_events():
    client = Client(get_pulsar_url())

    consumer = client.subscribe(
        topic="listing-information-events",
        subscription_name="listing-information-sub-properties",
        schema=AvroSchema(PropertyProcessedEvent),
    )

    while True:
        message = consumer.receive()
        try:
            consumer.acknowledge(message)
            event = message.value()
            dispatcher.send(event=event, signal=type(event).__name__)
        except:
            consumer.negative_acknowledge(message)
