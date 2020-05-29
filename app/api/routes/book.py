from flask import Blueprint, jsonify, abort, request
from api.constants import PAGE, PER_PAGE
from api.book import (addNewBook, editBookByID,
                      removeBookByID, getBookList, getBookByID, filterBooksBy)


bp = Blueprint("book_routes", __name__)


@bp.route("/add-book", methods=["POST"])
def addBook():
    data = request.get_json() or {}
    title = data.get("title")
    yearOfPublication = data.get("year_of_publication")
    genre = data.get("genre")
    authorID = data.get("author_id")
    addNewBook(title, yearOfPublication, genre, authorID)
    return jsonify(message="OK"), 200


@bp.route("/edit-book/<id>", methods=["PUT"])
def editBook(id):
    data = request.get_json() or {}
    title = data.get("title")
    yearOfPublication = data.get("year_of_publication")
    genre = data.get("genre")
    authorID = data.get("author_id")
    editBookByID(id, title, yearOfPublication, genre, authorID)
    return jsonify(message="OK"), 200


@bp.route("/remove-book/<id>", methods=["DELETE"])
def removeBook(id):
    removeBookByID(id)
    return jsonify(message="OK"), 200


@bp.route("/get-books", methods=["GET"])
def getBooks():
    data = request.get_json() or {}
    page = data.get("page") or PAGE
    perPage = data.get("per_page") or PER_PAGE
    books = getBookList(page, perPage)
    return jsonify(books=books), 200


@bp.route("/get-book/<id>", methods=["GET"])
def getBook(id):
    book = getBookByID(id)
    return jsonify(book=book), 200


@bp.route("/filter-books", methods=["GET"])
def filterBooks():
    data = request.get_json() or {}
    title = data.get("title")
    yearOfPublication = data.get("year_of_publication")
    genre = data.get("genre")
    authorName = data.get("author_name")
    page = data.get("page") or PAGE
    perPage = data.get("per_page") or PER_PAGE
    books = filterBooksBy(title, yearOfPublication,
                          genre, authorName, page, perPage)
    return jsonify(books=books), 200
