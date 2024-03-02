from pydispatch import dispatcher

from listings.modules.information.application.handlers import SalesHandler
from listings.modules.information.domain.events import SaleRegistered


dispatcher.connect(SalesHandler.handle_sale_registered, signal=SaleRegistered.__name__)
