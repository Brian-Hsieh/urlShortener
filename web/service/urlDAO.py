from web.url_shortener.shortener import UrlShortener
from web.static.constant import CODE_STRING_LENGTH
from web.model.model import Urls
from flask import url_for
from flask_restx import abort
from web import db

class UrlDAO():

    def __init__(self, db):
        self.shortener = UrlShortener()
        self.db = db

    def createShortUrl(self, longUrl):
        
        codeNumber = self.shortener.generateRand()

        #check if codeNumber already generated
        if Urls.query.filter_by(codeNumber = codeNumber).first():
            abort(500, "Duplicate code number found in database.")

        codeString = self.shortener.encode(codeNumber)

        shortUrl = url_for('routes.home', _external = True) + codeString

        #check if SHORT URL properly generated
        if len(shortUrl) >= len(longUrl):
            abort(500, "Encode error (Encoded URL longer than original URL)")

        db.session.add(Urls(longUrl,codeNumber))
        db.session.commit()

        response = {
            'longUrl': longUrl,
            'shortUrl': shortUrl
        }
        return response, 201

    def getLongUrl(self, shortUrl):

        codeString = self.shortener.getCodeString(shortUrl)

        #check if length of codeString is correct
        if len(codeString) != CODE_STRING_LENGTH:
            abort(404, "Decode error (Decoded URL not found)")

        codeNumber = self.shortener.decode(codeString)

        #check if codeNumber in database and return
        urlData = Urls.query.filter_by(codeNumber = codeNumber).first()
        if not urlData:
            abort(404, "Decode error (Decoded URL not found)")

        response = {
            'longUrl': urlData.longUrl,
            'shortUrl': shortUrl
        }
        return response, 200

urlDAO = UrlDAO(db)