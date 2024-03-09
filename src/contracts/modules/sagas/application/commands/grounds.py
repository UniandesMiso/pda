from dataclasses import dataclass

from contracts.seedwork.application.commands import Command, execute_command as command


class GroundCommand(Command): ...


@dataclass
class UpdateAmount(GroundCommand):
    property_id: str
    sale_id: str
    price: float
    currency: str


class UpdateAmountHandler:

    def handle(self, command: UpdateAmount):
        print("publicar comando a topico")


@command.register(UpdateAmount)
def execute_update_amount(command: UpdateAmount):
    handler = UpdateAmountHandler()
    return handler.handle(command)
