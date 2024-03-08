import logging
import traceback
from pulsar import Client
from pulsar.schema import AvroSchema
from contracts.seedwork.infrastructure.utils import get_pulsar_url
from contracts.modules.sales.infrastructure.schema.v1.events import SaleRegisteredEvent


def subscribe_2_events(app=None):
    client = None
    try:
        client = Client(get_pulsar_url())
        consumer = client.subscribe(
            topic="contracts-sales-events",
            subscription_name="contracts-sales-sub-self",
            schema=AvroSchema(SaleRegisteredEvent),
        )

        while True:
            message = consumer.receive()
            if process_message(message, app):
                consumer.acknowledge(message)
            else:
                consumer.negative_acknowledge(message)
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if client:
            client.close()


def process_message(message, app) -> bool:
    try:
        print(f"Received message: {message.value().data}")
        return True
    except:
        return False