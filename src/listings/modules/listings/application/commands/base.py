from listings.seedwork.application.commands import CommandHandler
from listings.modules.listings.infrastructure.repositories import SaleRepositoryGeneric


class BaseCommandHandler(CommandHandler):

    def __init__(self):
        self._repository = SaleRepositoryGeneric()

    @property
    def repository(self):
        return self._repository
