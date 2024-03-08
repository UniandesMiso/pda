from properties.seedwork.application.sagas import OrchestrationCoordinator, Start, Transaction, End
from properties.modules.sagas.application.commands.sales import RegisterSale
from properties.modules.sagas.domain.events.sales import SaleRegistered, SaleRegisterFailed

class GroundsCoordinator(OrchestrationCoordinator):

    def initialize_steps(self):
        self.steps = [
            Start(index=0),
            Transaction(index=1, command=RegisterSale, event=SaleRegistered, error=SaleRegisterFailed, compensation=DeleteSale),
            Transaction(index=2, command=RegisterSale, event=SaleRegistered, error=SaleRegisterFailed, compensation=DeleteSale),
            End(index=4)
        ]
