from listings.seedwork.application.queries import QueryHandler
from listings.modules.information.infrastructure.repositories import SaleRepositoryGeneric


class BaseQueryHandler(QueryHandler):

    def __init__(self):
        self._repository = SaleRepositoryGeneric()

    @property
    def repository(self):
        return self._repository
