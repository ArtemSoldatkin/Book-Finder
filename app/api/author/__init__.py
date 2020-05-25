from datetime import datetime
from flask import abort
from api.models import db
from api.models.author import Author


def addAuthor(name: str):
    """Add new author to DB"""
    # add birth and convert string to datetime
    if not name:
        abort(400)
    author = Author(name, birth=datetime.now())
    db.session.add(author)
    db.session.commit()


def editAuthorByID(id: int, name: str, birth: str):
    """Edit author by ID"""
    if not id:
        abort(400)
    author = Author.query.get(id)
    if not author:
        abort(404)
    if name:
        author.name = name
    if birth:
        author.birth = birth
    db.session.commit()


def removeAuthorByID(id: int):
    """Remove author from DB by ID"""
    Author.query.filter_by(id=id).delete()
    db.session.commit()


def getListOfAuthors() -> [Author]:
    """Get list of authors from DB"""
    authors = Author.query.all()
    return [author.serialize() for author in authors]

# add find authors
# change filter


def filterListOfAuthors(name: str, birth: datetime) -> [Author]:
    """Filter authors by name / birth"""
    authors = None
    if name and birth:
        authors = Author.query.filter_by(name=name, birth=birth)
    elif name:
        authors = Author.query.filter_by(name=name)
    elif birth:
        authors = Author.query.filter_by(birth=birth)
    if authors:
        return [author.serialize() for author in authors]
    abort(400)


def getAuthorByID(id: int) -> Author:
    """Get author from DB by ID"""
    if not id:
        abort(400)
    author = Author.query.get(id)
    if not author:
        abort(404)
    return author.serialize()
