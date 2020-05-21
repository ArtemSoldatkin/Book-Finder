#from api import db
from api.models import db
from api.models.author import Author


def addAuthor(name):

    author = Author(name)
    db.session.add(author)
    db.session.commit()


def getAuthors():

    authors = Author.query.all()
    return authors


def getAuthorByID(id):

    author = Author.query.get(id)
    return author
