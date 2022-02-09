from flask import Blueprint, render_template, jsonify, request
from url_shortener import shortener
from werkzeug.exceptions import abort

routes = Blueprint("routes", __name__)

@routes.route('/')
def home():
    return render_template("base.html")

@routes.route('/encode', methods=['POST'])
def encode():
    long_url = request.form['long_url']
    short_url = shortener.encode(long_url)
    return jsonify({
        'long_url': long_url, 
        'short_url': short_url
    }), 201

@routes.route('/decode', methods=['GET'])
def decode():
    short_url = request.args['short_url']
    long_url = shortener.decode(short_url)
    return jsonify({
        'long_url': long_url, 
        'short_url': short_url
    }), 200

@routes.errorhandler(404)
@routes.errorhandler(500)
def handleError(e):
    response = {
        'code': e.code,
        'name': e.name,
        'description': e.description
    }
    return jsonify(response), e.code