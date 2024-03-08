from pulsar import Client
from pulsar.schema import AvroSchema

from contracts.seedwork.infrastructure.utils import get_pulsar_url
from contracts.modules.sales.infrastructure.schema.v1.events import SaleRegisteredEvent


def subscribe_2_events():
    client = Client(get_pulsar_url())

    consumer = client.subscribe(
        topic="contracts-sales-events",
        subscription_name="contracts-sales-sub-self",
        schema=AvroSchema(SaleRegisteredEvent),
    )

    while True:
        message = consumer.receive()
        try:
            print(f"Received message: {message.value().data}")
            consumer.acknowledge(message)
        except:
            consumer.negative_acknowledge(message)
