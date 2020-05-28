from flask import abort
from api.models import db
from api.models.book import Book
from api.models.author import Author
from api.book.utils import checkYearOfPublication


def addNewBook(title: str, yearOfPublication: str, genre: str, authorID: int):
    """Add book to DB"""
    if not title or not checkYearOfPublication(yearOfPublication) or not genre or not authorID:
        abort(400)
    # TODO check author ID
    book = Book(title=title, yearOfPublication=yearOfPublication,
                genre=genre, authorID=authorID)
    db.session.add(book)
    db.session.commit()


def editBookByID(id: int, title: str, yearOfPublication: str, genre: str, authorID: int):
    """Edit book by ID"""
    book = Book.query.get(id)
    if not book:
        abort(404)
    if title:
        book.title = title
    if yearOfPublication:
        book.yearOfPublication = yearOfPublication
    if genre:
        book.genre = genre
    if authorID:
        book.authorID = authorID
    db.session.commit()


def removeBookByID(id: int):
    """Remove book from DB by ID"""
    Book.query.filter_by(id=id).delete()
    db.session.commit()


def getBookList(page: int, perPage: int) -> [Book]:
    """Get all books from DB"""
    books = Book.query.paginate(page=page, per_page=perPage)
    return [book.serialize() for book in books.items]


def getBookByID(id: int) -> Book:
    """Get book by ID from DB"""
    book = Book.query.get(id)
    if not book:
        abort(404)
    return book.serialize()


def filterBooksBy() -> [Book]:
    """Filter books by author/title/year of publication/genre"""
    pass
