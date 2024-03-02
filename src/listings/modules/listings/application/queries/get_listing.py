from dataclasses import dataclass

from contracts.seedwork.application.queries import Query, QueryResult, execute_query as query
from contracts.modules.sales.application.mappers import SaleMapper
from contracts.modules.sales.application.queries.base import BaseQueryHandler


@dataclass
class GetListing(Query):
    id: str


class GetListingHandler(BaseQueryHandler):

    def handle(self, query: GetListing) -> QueryResult:
        sale = self.repository.get_by_id(query.id)
        mapper = SaleMapper()
        return QueryResult(data=mapper.entity_2_dto(sale))


@query.register(GetListing)
def execute_get_sale(query: GetListing):
    handler = GetListingHandler()
    return handler.handle(query)
