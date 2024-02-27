from pydispatch import dispatcher

from properties.modules.grounds.application.handlers import GroundsHandler
from properties.modules.grounds.infrastructure.schema.v1.events import SaleRegisteredEvent


dispatcher.connect(GroundsHandler.handle_sale_registered, signal=SaleRegisteredEvent.__name__)
