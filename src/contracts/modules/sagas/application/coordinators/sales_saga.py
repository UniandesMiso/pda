from contracts.seedwork.application.commands import Command
from contracts.seedwork.application.sagas import OrchestrationCoordinator, Start, Transaction, End
from contracts.seedwork.domain.events import DomainEvent
from contracts.modules.sagas.application.factories import FactoryCommands
from contracts.modules.sagas.application.commands.grounds import UpdateAmount
from contracts.modules.sagas.domain.events.grounds import AmountUpdated, AmountUpdateFailed
from contracts.modules.sales.application.commands.register_sale import RegisterSale
from contracts.modules.sales.application.commands.delete_sale import DeleteSale
from contracts.modules.sales.domain.events import SaleRegistered, SaleRegisterFailed

class SalesCoordinator(OrchestrationCoordinator):

    def __init__(self):
        self.factory = FactoryCommands()

    def initialize_steps(self):
        self.steps = [
            Start(index=0),
            Transaction(index=1, command=RegisterSale, event=SaleRegistered, error=SaleRegisterFailed, compensation=DeleteSale),
            Transaction(index=2, command=UpdateAmount, event=AmountUpdated, error=AmountUpdateFailed, compensation=DeleteSale),
            End(index=4)
        ]

    def start(self): ...

    def finish(self): ...

    def save_log(self, message): ...

    def build_command(self, event: DomainEvent, command_type: type) -> Command:
        return self.factory.create_object(event)
        

def listen_event(event):
    if isinstance(event, DomainEvent):
        coordinator = SalesCoordinator()
        coordinator.initialize_steps()
        coordinator.process_event(event)
