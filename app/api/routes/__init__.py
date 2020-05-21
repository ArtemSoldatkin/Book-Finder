from flask import Blueprint, jsonify, current_app as app

bp = Blueprint("errors", __name__)


@bp.app_errorhandler(400)
def handle400(err):
    app.logger.error(err)
    return jsonify(message="Wrong parameters"), 400
