from properties.seedwork.application.handlers import Handler
from properties.modules.grounds.infrastructure.dispatchers import Dispatcher


class GroundsHandler(Handler):

    @staticmethod
    def handle_amount_updated(event):
        dispatcher = Dispatcher()
        dispatcher.send_event("grounds-events", event)
