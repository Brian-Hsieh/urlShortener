from flask import Blueprint, render_template, jsonify, request
from web.service import urlDAO

routes = Blueprint("routes", __name__)

@routes.route('/')
def home():
    pass
    # return render_template("base.html")

@routes.route('/encode/<longUrl>', methods=['POST'])
def encode():
    '''Encode long URL to short URL'''
    return urlDAO.createShortUrl(longUrl), 201

@routes.route('/decode/<shortUrl>', methods=['GET'])
def decode():
    return urlDAO.getLongUrl(shortUrl)

@routes.errorhandler(404)
@routes.errorhandler(500)
def handleError(e):
    response = {
        'code': e.code,
        'name': e.name,
        'description': e.description
    }
    return jsonify(response), e.code