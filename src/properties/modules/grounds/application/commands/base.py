from properties.seedwork.application.commands import CommandHandler
from properties.modules.grounds.infrastructure.repositories import GroundRepositoryGeneric


class BaseCommandHandler(CommandHandler):

    def __init__(self):
        self._repository = GroundRepositoryGeneric()

    @property
    def repository(self):
        return self._repository
