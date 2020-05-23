from datetime import datetime
from flask import abort
from api.models import db
from api.models.author import Author


def addAuthor(name):
    author = Author(name, birth=datetime.now())
    db.session.add(author)
    db.session.commit()


def getAuthors():
    authors = Author.query.all()
    return [author.serialize() for author in authors]


def getAuthorByID(id):
    if not id:
        abort(400)
    author = Author.query.get(id)
    if not author:
        abort(404)
    return author.serialize()
