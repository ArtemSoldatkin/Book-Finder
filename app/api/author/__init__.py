from flask import abort
from api.utils import checkDate
from api.models import db
from api.models.author import Author


def addAuthor(name: str, birth: str):
    """Add new author to DB"""
    if not name or not checkDate(birth):
        abort(400)
    author = Author(name, birth)
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


def getListOfAuthors(page: int, perPage: int) -> [Author]:
    """Get list of authors from DB"""
    authors = Author.query.paginate(page=page, per_page=perPage)
    return [author.serialize() for author in authors.items]


def filterListOfAuthors(name: str, birth: str, page: int, perPage: int) -> [Author]:
    """Filter authors by name / birth"""
    authors = Author.query.filter(Author.name.ilike(
        f"%{name}%")).filter(Author.birth.ilike(f"%{birth}%")).paginate(page=page, per_page=perPage)
    if authors:
        return [author.serialize() for author in authors.items]
    abort(400)


def getAuthorByID(id: int) -> Author:
    """Get author from DB by ID"""
    if not id:
        abort(400)
    author = Author.query.get(id)
    if not author:
        abort(404)
    return author.serialize()
