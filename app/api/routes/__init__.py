from flask import Blueprint, jsonify, current_app as app

bp = Blueprint("errors", __name__)


@bp.app_errorhandler(400)
def handle400(err):
    app.logger.error(err)
    return jsonify(message=err.description or "Wrong parameters"), 400


@bp.app_errorhandler(404)
def handle404(err):
    app.logger.error(err)
    return jsonify(message=err.description or "Not found"), 404


@bp.app_errorhandler(500)
def handle500(err):
    app.logger.error(err)
    return jsonify(message=err.description or "Server error"), 500
