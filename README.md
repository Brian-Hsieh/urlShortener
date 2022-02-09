# ShortLink

ShortLink is an URL shortener service written in [flask](https://flask.palletsprojects.com/en/2.0.x/) which provides 2 endpoints on encoding and decoding the URL. The original long URL can be encoded into a short URL and the shortened URL can be decoded into the original URL. Both endpoints return the JSON to the web page including the original URL and the shortened URL.
## Installation
---
Create a virtual environment if needed

Install required packages with pip:
```
pip install -r requirements.txt
```
## Unit testing
---
Unittest is required to run the test. It is included in standard library in Python 2.1 and above.

Test the service with:
```
python test.py
```
## Execution
---
Start the service with:
```
python api.py
```
Open the web page with URL ```http://127.0.0.1:5000``` or press ```Ctrl``` and click on the link in terminal.

- Encoding
    - A long URL is expected in the input field
    - Return JSON with long URL and encoded short URL
    - Return server error in JSON if server cannot encode URL properly or the original URL is too short
- Decoding
    - A short encoded URL is expected in the input field
    - Return JSON with decoded long URL and short URL
    - Return not found error in JSON if decoded URL does not present in database

If one would like to inspect the database, run in terminal with: ```sqlite3 web/urls.sqlite3```, then check items in the table with: ```select * from urls;```

> **Note:** Since no home button is provided, please return to the home page by going back to the previous page.
