from flask import Blueprint, jsonify, request

from properties.seedwork.application.queries import execute_query
from properties.seedwork.application.commands import execute_command
from properties.modules.grounds.application.mappers import GroundMapperDTO
from properties.modules.grounds.application.commands.register_ground import RegisterGround
from properties.modules.grounds.application.queries.get_ground import GetGround


bp = Blueprint("grounds", __name__, url_prefix="/grounds")


@bp.route("/", methods=["POST"])
def register_ground():
    mapper = GroundMapperDTO()
    ground_dto = mapper.dict_2_dto(request.json)

    command = RegisterGround(
        address=ground_dto.address,
        width=ground_dto.width,
        length=ground_dto.length,
        location=ground_dto.location,
        price=ground_dto.price,
        currency=ground_dto.currency
    )

    result = execute_command(command)
    return jsonify(mapper.dto_2_dict(result.data))


@bp.route("/", methods=["GET"])
@bp.route("/<id>", methods=["GET"])
def get_ground(id=None):
    if not id:
        return jsonify({"message": "The ground ID is required"}), 400

    query = GetGround(id=id)
    result = execute_query(query)

    if not result.data:
        return jsonify({"message": f"The ground with ID {id} does not exist"}), 400

    mapper = GroundMapperDTO()
    return jsonify(mapper.dto_2_dict(result.data))
