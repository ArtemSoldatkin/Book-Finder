from flask import Blueprint, jsonify, abort, request
from api.author import (addAuthor, editAuthorByID,
                        removeAuthorByID, getListOfAuthors, getAuthorByID)

bp = Blueprint("author_routes", __name__)


@bp.route("/add-author", methods=["POST"])
def addNewAuthor():
    data = request.get_json()
    name = data.get("name")
    addAuthor(name)
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
    authors = getListOfAuthors()
    return jsonify(authorList=authors), 200

# Add filters to authors by name and birth


@bp.route("/get-author/<id>", methods=["GET"])
def getAuthor(id):
    author = getAuthorByID(id)
    return jsonify(author=author)
