from pydispatch import dispatcher

from properties.modules.grounds.application.handlers import GroundsHandler
from properties.modules.grounds.domain.events import AmountUpdated


dispatcher.connect(GroundsHandler.handle_amount_updated, signal=AmountUpdated.__name__)
