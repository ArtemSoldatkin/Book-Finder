from flask import Blueprint, jsonify

bp = Blueprint("creator_routes", __name__)


@bp.route("/add-creator", methods=["POST"])
def addCreator():
    # TODO
    return jsonify(message="OK")


@bp.route("/sign-in", methods=["GET"])
def signIn():
    # TODO
    return jsonify(message="OK")
