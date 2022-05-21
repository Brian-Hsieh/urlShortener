from flask_restx import Namespace, fields

class UrlDTO:

    route = Namespace('url', description = 'Url manipulation.')
    url = route.model('url', {
        'longUrl': fields.String(description = 'The long url.'),
        'shortUrl': fields.String(description = 'The short url.')
    })

