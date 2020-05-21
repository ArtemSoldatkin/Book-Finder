#import os
from flask import Flask
from api.models import db

from api.routes.author import bp as author
from api.routes import bp as errors

app = Flask(__name__)
app.config.from_object("api.config.Config")
db.init_app(app)

app.register_blueprint(errors)
app.register_blueprint(author)
