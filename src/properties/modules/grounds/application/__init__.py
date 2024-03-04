from pydispatch import dispatcher

from properties.modules.grounds.application.handlers import GroundsHandler
from properties.modules.grounds.infrastructure.schema.v1.events import SaleRegisteredEvent, PropertyProcessedEvent


dispatcher.connect(GroundsHandler.handle_sale_registered, signal=SaleRegisteredEvent.__name__)
dispatcher.connect(GroundsHandler.handle_property_processed, signal=PropertyProcessedEvent.__name__)
