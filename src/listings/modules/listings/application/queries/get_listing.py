from dataclasses import dataclass

from listings.seedwork.application.queries import Query, QueryResult, execute_query as query
from listings.modules.information.application.mappers import InformationMapper


@dataclass
class GetListing(Query):
    id: str


class GetListingHandler(BaseQueryHandler):

    def handle(self, query: GetListing) -> QueryResult:
        sale = self.repository.get_by_id(query.id)
        mapper = InformationMapper()
        return QueryResult(data=mapper.entity_2_dto(sale))


@query.register(GetListing)
def execute_get_sale(query: GetListing):
    handler = GetListingHandler()
    return handler.handle(query)
