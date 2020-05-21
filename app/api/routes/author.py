from flask import Blueprint, jsonify, abort, request
from api.author import (addAuthor, getAuthors, getAuthorByID)

bp = Blueprint("author_routes", __name__)


@bp.route("/add-author", methods=["POST"])
def addNewAuthor():
    data = request.get_json()
    name = data.get("name")
    if not name:
        abort(400)
    addAuthor(name)
    return jsonify(message="OK"), 200


@bp.route("/get-authors", methods=["GET"])
def getAuthorsList():
    authors = getAuthors()
    for author in authors:
        print(author.name, flush=True)
    return jsonify(message="OK"), 200


@bp.route("/get-author/:id", methods=["GET"])
def getAuthor():
    pass
