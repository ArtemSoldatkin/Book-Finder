from api.models import db


class Creator(db.Model):
    # Role with options for adding / editing authors and books
    __tablename__ = "creator"
    login = db.Column(db.String(32), primary_key=True)
    password = db.Column(db.String(32), nullable=False)

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
