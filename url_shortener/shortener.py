from web.static.constant import *
from web.model import Urls
from werkzeug.exceptions import InternalServerError, NotFound
import random

class UrlShortener():
    '''
    This provides the method to encode and decode the url.
    Store the searched url into a dictionary
    '''
    def __init__(self, db):
        self.db = db
        random.seed(SEED) #seeding for code number

    def encode(self, long_url):
        '''
        Encode long URL with randomly-generated code_number and KEY to code_string
        '''
        code_number = random.randint(1,CODE_NUMBER_UPPER_LIMIT)

        #check if code_number already generated
        if Urls.query.filter_by(code_number = code_number).first():
            raise InternalServerError(description = 'Encode error (Duplicate encoded URL found)')

        #start encoding
        code_string = ""
        num = code_number
        while(num > 0):
            code_string = code_string + KEY[num%len(KEY)]
            num //= len(KEY)
        code_string = code_string[::-1]

        short_url = "https://" + SHORT_URL_PREFIX + code_string

        #check if SHORT URL properly generated
        if len(short_url) >= len(long_url):
            raise InternalServerError(description = 'Encode error (Encoded URL longer than original URL)')
        self.db.session.add(Urls(long_url,code_number))
        self.db.session.commit()
        return short_url

    def decode(self, short_url):
        '''
        Decode code_string to code_number then look up in the database for long URL
        '''
        code_string = short_url.split('/')[-1]

        #check if length of code_string is correct
        if len(code_string) != CODE_STRING_LENGTH:
            raise NotFound(description = 'Decode error (Decoded URL not found)')

        #start decode
        code_number = 0
        for code in code_string:
            code_number = code_number*len(KEY) + KEY.index(code) #better access possible
        
        #check if code_number in database and return
        url_data = Urls.query.filter_by(code_number = code_number).first()
        if not url_data:
            raise NotFound(description = 'Decode error (Decoded URL not found)')
        return url_data.long_url 