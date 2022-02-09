from .shortener import UrlShortener
from web import db

shortener = UrlShortener(db)