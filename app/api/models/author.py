from api.models import db, datetimeToJson
from api.models.book import Book


class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birth = db.Column(db.DateTime, nullable=False)
    books = db.relationship("Book")

    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

    def serialize(self):
        return {"id": self.id, "name": self.name, "birth": datetimeToJson(self.birth)}
