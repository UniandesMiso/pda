from datetime import datetime
from pulsar import Client
from pulsar.schema import AvroSchema

from contracts.seedwork.infrastructure.utils import get_pulsar_url
from contracts.modules.sales.infrastructure.schema.v1.events import SaleRegisteredEvent, SaleRegisteredPayload


class Dispatcher:

    def _send_message(self, topic, message, schema):
        client = Client(get_pulsar_url())
        producer = client.create_producer(topic, schema=schema)
        producer.send(message)
        client.close()

    def send_event(self, topic, event):
        payload = SaleRegisteredPayload(
            sale_id=str(event.id),
            price=event.price,
            currency=event.currency,
            executed_at=int(event.executed_at.timestamp())
        )

        message = SaleRegisteredEvent(data=payload)
        # print(message)
        # print(message.data)
        self._send_message(topic, message, AvroSchema(SaleRegisteredEvent))
