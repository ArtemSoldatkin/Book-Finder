from api.models import db


class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    books = db.relationship("Book")

    def __init__(self, name):
        self.name = name


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    authorID = db.Column(db.Integer, db.ForeignKey("authors.id"))

    def __init__(self, title, authorID):
        self.title = title
        self.authorID = authorID
