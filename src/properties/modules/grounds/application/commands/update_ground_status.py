from dataclasses import dataclass

from properties.seedwork.application.commands import Command, CommandResult, execute_command as command
from properties.modules.grounds.application.dto import GroundDTO
from properties.modules.grounds.application.mappers import GroundMapper
from properties.modules.grounds.application.commands.base import BaseCommandHandler


@dataclass
class UpdateGroundStatus(Command):
    id: str


class UpdateGroundStatusHandler(BaseCommandHandler):

    def handle(self, command: UpdateGroundStatus) -> CommandResult:
        ground_dto = GroundDTO(id=command.id, status="SOLD")

        mapper = GroundMapper()
        ground = mapper.dto_2_entity(ground_dto)

        self.repository.update(ground)
        return CommandResult(data=mapper.entity_2_dto(ground))


@command.register(UpdateGroundStatus)
def execute_update_ground_status(command: UpdateGroundStatus):
    handler = UpdateGroundStatusHandler()
    return handler.handle(command)
