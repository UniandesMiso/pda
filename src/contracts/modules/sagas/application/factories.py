from dataclasses import dataclass

from contracts.seedwork.application.commands import Command
from contracts.seedwork.domain.events import DomainEvent
from contracts.modules.sales.application.commands.delete_sale import DeleteSale
from contracts.modules.sales.domain.events import SaleRegistered
from contracts.modules.sagas.application.commands.grounds import UpdateAmount
from contracts.modules.sagas.domain.events.grounds import AmountUpdateFailed


@dataclass
class FactoryCommands():

    def create_object(self, event: DomainEvent) -> Command:
        if type(event) == SaleRegistered.__name__:
            return UpdateAmount(
                property_id=event.property_id,
                price=event.price,
                currency=event.currency
            )

        if type(event) == AmountUpdateFailed.__name__:
            return DeleteSale(id=event.sale_id)

        else:
            raise Exception("The factory does not exist for the requested type")
