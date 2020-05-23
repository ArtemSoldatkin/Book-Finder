from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from json import dumps


db = SQLAlchemy()


def jsonDefault(value):
    if isinstance(value, datetime):
        return dict(year=value.year, month=value.month, day=value.day, hour=value.hour, minute=value.minute)
    else:
        return value.__dict__


def datetimeToJson(value):
    return dumps(value, default=jsonDefault)
