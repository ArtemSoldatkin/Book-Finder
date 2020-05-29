#import os
from flask import Flask
from api.models import db

from api.routes.author import bp as author
from api.routes.book import bp as book
from api.routes import bp as errors
from api.routes.creator import bp as creator

app = Flask(__name__)
app.config.from_object("api.config.Config")
db.init_app(app)

app.register_blueprint(errors)
app.register_blueprint(author)
app.register_blueprint(book)
app.register_blueprint(creator)
