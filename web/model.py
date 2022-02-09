from . import db
from datetime import datetime

class Urls(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    long_url = db.Column(db.String(1000))
    code_number = db.Column(db.Integer, unique = True)
    date_created = db.Column(db.DateTime, default = datetime.now)

    def __init__(self, long_url, code_number):
        self.long_url = long_url
        self.code_number = code_number
