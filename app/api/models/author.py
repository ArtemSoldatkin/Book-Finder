from api.models import db
from api.models.book import Book


class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    books = db.relationship("Book")

    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

    def serialize(self):
        return {"id": self.id, "name": self.name, "birth": self.birth}
