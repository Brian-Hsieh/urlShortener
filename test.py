import unittest
from flask import url_for
from flask_testing import TestCase
from web import db, create_app
from web.model import Urls

class UrlTest(TestCase):

    def create_app(self):

        app = create_app()
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///../test.sqlite3',
            TESTING = True
        )
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self): 
        db.session.remove()
        db.drop_all()

    def test_db(self):
        '''
        check if database properly store the data
        '''
        urls = Urls('long_url', code_number = 123)
        db.session.add(urls)
        db.session.commit()
        self.assertIn(urls, db.session)
    
    def test_home_page(self):
        '''
        check if home page rendered properly
        '''
        with self.app.test_client() as test_client:
            rv = test_client.get('/')
            self.assertEqual(rv.status_code, 200)
    
    def test_encoding(self):
        '''
        check if correct response is returned given different long URLs
        '''
        url_encode = url_for('routes.encode')
        with self.app.test_client() as test_client:

            #500 expected if long URL shares same code_string with other URL in databse
            old_urls = Urls('long_url', code_number = 611178003) #deterministic number from randint with seeding
            db.session.add(old_urls)
            db.session.commit()
            rv = test_client.post(url_encode, data = dict(long_url = 'https://longurl.com/longurllongurl'))
            self.assertEqual(rv.status_code, 500)
            self.assertIn('Duplicate encoded URL found', rv.json['description'])
            
            #500 expected if shortened URL longer than original short URL
            rv = test_client.post(url_encode, data = dict(long_url = 'https://short/'))
            self.assertEqual(rv.status_code, 500)
            self.assertIn('Encoded URL longer than original URL', rv.json['description'])

            #201 expected if no conflicts and URL is shorter
            rv = test_client.post(url_encode, data = dict(long_url = 'https://verylongurl.com/verylongurl'))
            self.assertEqual(rv.status_code, 201)

    def test_decoding(self):
        '''
        check if correct response is returned given different short URLs
        '''
        url_encode = url_for('routes.encode')
        url_decode = url_for('routes.decode')

        with self.app.test_client() as test_client:

            #404 expected if searching in empty database or searching for an unencoded URL with code_string of correct length
            rv = test_client.get('/decode', query_string = dict(short_url = 'https://short/short'))
            self.assertEqual(rv.status_code, 404)
            self.assertIn('Decoded URL not found', rv.json['description'])

            #404 expected if searching for an URL with code_string of incorrect length
            rv = test_client.get('/decode', query_string = dict(short_url = 'https://short/shorts'))
            self.assertEqual(rv.status_code, 404)
            self.assertIn('Decoded URL not found', rv.json['description'])

            # 200 expected if encoded URL is found
            rv = test_client.post(url_encode, data = dict(long_url = 'https://longurl.com/longurl'))
            short_url = rv.json['short_url']
            rv = test_client.get(url_decode, query_string = dict(short_url = short_url))
            self.assertEqual(rv.status_code, 200)

if __name__ == "__main__":
    unittest.main()