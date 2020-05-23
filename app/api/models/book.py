from api.models import db


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    yearOfPublication = db.Column(db.String(4), nullable=False)
    genre = db.Column(db.String(64), nullable=False)
    authorID = db.Column(db.Integer, db.ForeignKey("authors.id"))

    def __init__(self, title, yearOfPublication, genre, authorID):
        self.title = title
        self.yearOfPublication = yearOfPublication
        self.genre = genre
        self.authorID = authorID
