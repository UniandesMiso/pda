from dataclasses import dataclass
from pydispatch import dispatcher

from contracts.config.db import db
from contracts.seedwork.application.commands import Command, CommandResult, execute_command as command
from contracts.modules.sales.application.dto import SaleDTO
from contracts.modules.sales.application.mappers import SaleMapper
from contracts.modules.sales.application.commands.base import BaseCommandHandler


@dataclass
class RegisterSale(Command):
    price: float
    currency: str
    executed_at: str


class RegisterSaleHandler(BaseCommandHandler):

    def handle(self, command: RegisterSale) -> CommandResult:
        contract_dto = SaleDTO(
            price=command.price,
            currency=command.currency,
            executedAt=command.executed_at,
        )

        mapper = SaleMapper()
        sale = mapper.dto_2_entity(contract_dto)

        sale.register_sale()
        self.repository.create(sale)
        db.session.commit()

        for event in sale.events:
            dispatcher.send(event=event, signal=type(event).__name__)

        return CommandResult(data=mapper.entity_2_dto(sale))


@command.register(RegisterSale)
def execute_register_sale(command: RegisterSale):
    handler = RegisterSaleHandler()
    return handler.handle(command)
