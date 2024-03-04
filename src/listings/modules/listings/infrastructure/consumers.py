from pulsar import Client, ConsumerType
from pulsar.schema import AvroSchema

from listings.seedwork.infrastructure.utils import get_pulsar_url
from listings.modules.information.infrastructure.schema.v1.events import SaleRegisteredEvent


def subscribe_2_events():
    client = Client(get_pulsar_url())

    consumer = client.subscribe(
        topic="information-events",
        subscription_name="listings-information-sub",
        schema=AvroSchema(SaleRegisteredEvent),
    )

    while True:
        message = consumer.receive()
        try:
            print(f"Received message: {message.value().data}")
            consumer.acknowledge(message)
        except:
            consumer.negative_acknowledge(message)
