from flask import Blueprint, jsonify, request

from listings.seedwork.application.queries import execute_query
from listings.seedwork.application.commands import execute_command
from listings.modules.listings.application.mappers import ListingMapperDTO
from listings.modules.listings.application.queries.get_listing import GetListing
from listings.modules.listings.application.commands.process_listing import ProcessListing

bp = Blueprint("listings", __name__, url_prefix="/listings")

@bp.route("/", methods=["POST"])
def process_listing():
    mapper = ListingMapperDTO()
    listing_dto = mapper.dict_2_dto(request.json)

    command = ProcessListing(
        properties=listing_dto.properties,
        executed_at=listing_dto.executedAt,
    )

    result = execute_command(command)
    return jsonify(mapper.dto_2_dict(result.data))


@bp.route("/<id>", methods=["GET"])
def get_listing(id=None):
    if not id:
        return jsonify({"message": "The listing ID is required"}), 400

    query = GetListing(id=id)
    result = execute_query(query)

    mapper = SaleMapperDTO()
    return jsonify(mapper.dto_2_dict(result.data))
