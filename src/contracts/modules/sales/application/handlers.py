from contracts.seedwork.application.handlers import Handler

from contracts.modules.sales.infrastructure.dispatchers import Dispatcher


class SalesHandler(Handler):

    @staticmethod
    def handle_sale_registered(event):
        dispatcher = Dispatcher()
        dispatcher.send_event("sales-events", event)
