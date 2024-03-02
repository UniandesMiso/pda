from dataclasses import dataclass

from properties.seedwork.application.commands import Command, CommandResult, execute_command as command
from properties.modules.grounds.application.dto import GroundDTO
from properties.modules.grounds.application.mappers import GroundMapper
from properties.modules.grounds.application.commands.base import BaseCommandHandler


@dataclass
class UpdateGroundPrice(Command):
    id: str
    price: float
    currency: str


class UpdateGroundPriceHandler(BaseCommandHandler):

    def handle(self, command: UpdateGroundPrice) -> CommandResult:
        ground_dto = GroundDTO(
            id=command.id,
            price=command.price,
            currency=command.currency
        )

        mapper = GroundMapper()
        ground = mapper.dto_2_entity(ground_dto)

        self.repository.update(ground)
        return CommandResult(data=mapper.entity_2_dto(ground))


@command.register(UpdateGroundPrice)
def execute_update_ground_status(command: UpdateGroundPrice):
    handler = UpdateGroundPriceHandler()
    return handler.handle(command)
