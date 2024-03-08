from dataclasses import dataclass

from properties.seedwork.application.commands import Command, CommandResult, execute_command as command
from properties.modules.grounds.application.dto import GroundDTO
from properties.modules.grounds.application.mappers import GroundMapper
from properties.modules.grounds.application.commands.base import BaseCommandHandler


@dataclass
class UpdateGroundAmount(Command):
    id: str
    price: float
    currency: str


class UpdateGroundAmountHandler(BaseCommandHandler):

    def handle(self, command: UpdateGroundAmount) -> CommandResult:
        ground_dto = GroundDTO(
            id=command.id,
            price=command.price,
            currency=command.currency
        )

        mapper = GroundMapper()
        ground = mapper.dto_2_entity(ground_dto)

        self.repository.update(ground)
        return CommandResult(data=mapper.entity_2_dto(ground))


@command.register(UpdateGroundAmount)
def execute_update_ground_status(command: UpdateGroundAmount):
    handler = UpdateGroundAmountHandler()
    return handler.handle(command)
