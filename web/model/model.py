from web import db
from datetime import datetime

class Urls(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    longUrl = db.Column(db.String(1000))
    codeNumber = db.Column(db.Integer, unique = True)
    dateCreated = db.Column(db.DateTime, default = datetime.now)

    def __init__(self, longUrl, codeNumber):
        self.longUrl = longUrl
        self.codeNumber = codeNumber
