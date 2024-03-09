from dataclasses import dataclass
from pydispatch import dispatcher

from properties.config.db import db
from properties.seedwork.application.commands import Command, CommandResult, execute_command as command
from properties.modules.grounds.application.dto import GroundDTO
from properties.modules.grounds.application.mappers import GroundMapper
from properties.modules.grounds.application.commands.base import BaseCommandHandler


@dataclass
class UpdateAmount(Command):
    id: str
    price: float
    currency: str


class UpdateAmountHandler(BaseCommandHandler):

    def handle(self, command: UpdateAmount) -> CommandResult:
        ground_dto = GroundDTO(
            id=command.id,
            price=command.price,
            currency=command.currency
        )

        mapper = GroundMapper()
        ground = mapper.dto_2_entity(ground_dto)

        ground.update_amount()
        self.repository.update(ground)

        for event in ground.events:
            dispatcher.send(event=event, signal=type(event).__name__)

        return CommandResult(data=mapper.entity_2_dto(ground))


@command.register(UpdateAmount)
def execute_update_ground_status(command: UpdateAmount):
    handler = UpdateAmountHandler()
    return handler.handle(command)
