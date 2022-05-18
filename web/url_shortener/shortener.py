from web.static.constant import *
import random

class UrlShortener():
    '''
    This provides the method to encode and decode the url.
    Store the searched url into a dictionary
    '''
    def __init__(self):
        random.seed(SEED) #seeding for code number

    def encode(self, codeNumber):
        '''
        Encode long URL with randomly-generated codeNumber and KEY to short URL
        '''
        codeString = ""
        num = codeNumber
        while(num > 0):
            codeString = codeString + KEY[num%len(KEY)]
            num //= len(KEY)
        codeString = codeString[::-1]

        return codeString

    def decode(self, codeString):
        '''
        Decode codeString to codeNumber then look up in the database for long URL
        '''
        codeNumber = 0
        for code in codeString:
            codeNumber = codeNumber*len(KEY) + KEY.index(code) #better access possible

        return codeNumber


    def generateRand(self):
        return random.randint(1, CODE_NUMBER_UPPER_LIMIT)


    def getCodeString(self, shortUrl):
        return shortUrl.split('/')[-1]