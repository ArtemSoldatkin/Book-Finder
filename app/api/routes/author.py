from flask import Blueprint, jsonify, abort, request
from api.constants import PAGE, PER_PAGE
from api.author import (addAuthor, editAuthorByID,
                        removeAuthorByID, getListOfAuthors, getAuthorByID, filterListOfAuthors)


bp = Blueprint("author_routes", __name__)


@bp.route("/add-author", methods=["POST"])
def addNewAuthor():
    data = request.get_json()
    name = data.get("name")
    birth = data.get("birth")
    addAuthor(name, birth)
    return jsonify(message="OK"), 200


@bp.route("/edit-author/<id>", methods=["PUT"])
def editAuthor(id):
    data = request.get_json()
    name = data.get("name")
    birth = data.get("birth")
    editAuthorByID(id, name, birth)
    return jsonify(message="OK"), 200


@bp.route("/remove-author/<id>", methods=["DELETE"])
def removeAuthor(id):
    removeAuthorByID(id)
    return jsonify(message="OK"), 200


# Add pages (max count of author per request)
@bp.route("/get-authors", methods=["GET"])
def getAuthors():
    data = request.get_json()
    page = data.get("page") or PAGE
    perPage = data.get("per_page") or PER_PAGE
    authors = getListOfAuthors(page, perPage)
    return jsonify(authors=authors), 200


@bp.route("/filter-authors", methods=["GET"])
def filterAuthors():
    data = request.get_json()
    name = data.get("name") or ""
    birth = data.get("birth") or ""
    page = data.get("page") or PAGE
    perPage = data.get("per_page") or PER_PAGE
    authors = filterListOfAuthors(name, birth, page, perPage)
    return jsonify(authors=authors), 200


@bp.route("/get-author/<id>", methods=["GET"])
def getAuthor(id):
    author = getAuthorByID(id)
    return jsonify(author=author)
