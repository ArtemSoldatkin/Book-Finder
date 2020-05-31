from flask import abort, current_app as app
from api.models import db
from api.models.book import Book
from api.models.author import Author
from api.book.utils import checkYearOfPublication


def addNewBook(title: str, yearOfPublication: str, genre: str, authorID: int):
    """Add book to DB"""
    if not title or not checkYearOfPublication(yearOfPublication) or not genre or not authorID:
        abort(400)
    if not Author.query.get(authorID):
        abort(404, "Author is not found")
    book = Book(title=title, yearOfPublication=yearOfPublication,
                genre=genre, authorID=authorID)
    db.session.add(book)
    db.session.commit()
    app.logger.info(f"New book with id: {book.id} added")


def editBookByID(id: int, title: str, yearOfPublication: str, genre: str, authorID: int):
    """Edit book by ID"""
    if not id:
        abort(400)
    book = Book.query.get(id)
    if not book:
        abort(404, "Book is not found")
    if title:
        book.title = title
    if yearOfPublication:
        book.yearOfPublication = yearOfPublication
    if genre:
        book.genre = genre
    if authorID:
        book.authorID = authorID
    db.session.commit()
    app.logger.info(f"The book {id} has been edited")


def removeBookByID(id: int):
    """Remove book from DB by ID"""
    Book.query.filter_by(id=id).delete()
    db.session.commit()
    app.logger.info(f"The book {id} has been removed")


def getBookList(page: int, perPage: int) -> [Book]:
    """Get all books from DB"""
    books = Book.query.paginate(page=page, per_page=perPage)
    return [book.serialize() for book in books.items]


def getBookByID(id: int) -> Book:
    """Get book by ID from DB"""
    if not id:
        abort(400)
    book = Book.query.get(id)
    if not book:
        abort(404, "Book is not found")
    return book.serialize()


def filterBooksBy(title: str, yearOfPublication: str, genre: str, authorName: str, page: int, perPage: int) -> [Book]:
    """Filter books by author/title/year of publication/genre"""
    books = Book.query.filter(Book.title.ilike(f"%{title}%")).filter(Book.yearOfPublication.ilike(
        f"%{yearOfPublication}%")).filter(Book.genre.ilike(f"%{genre}%")).filter(Book.author.name.ilike(f"%{authorName}%")).paginate(page=page, per_page=perPage)
    if books:
        return [book.serialize() for book in books.items]
    abort(400)
