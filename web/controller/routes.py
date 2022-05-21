from flask import jsonify, request
from flask_restx import Resource
from web.service.urlDAO import urlDAO
from web.utils.urlDTO import UrlDTO

route = UrlDTO.route
url = UrlDTO.url

@route.route('/encode')
class Encode(Resource):

    @route.doc('encode long url')
    @route.response(201, 'Url successfully encoded.')
    @route.marshal_with(url)
    def post(self):
        '''Encode long url to short url'''
        longUrl = request.json
        return urlDAO.createShortUrl(longUrl = longUrl)

@route.route('/decode')
class Decode(Resource):

    @route.doc('decode short url')
    @route.response(404, 'No corresponding long url being found.')
    @route.marshal_with(url)
    def get(self):
        '''Decode short url to long url'''
        shortUrl = request.json
        return urlDAO.getLongUrl(shortUrl = shortUrl)