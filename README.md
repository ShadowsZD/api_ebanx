# api_ebanx
Simple API for ebanx test
=========================

How to use it:
--------------

First install dependency:
```
pip install flask
```

Then run it with:
```
export FLASK_APP=api
flask run
```

or alternatively:
```
python api/api.py
```

Testing the API:
----------------
You can test the api using sending request on curl such as:

```
curl --location --request POST 'http://127.0.0.1:5000/event' \
--header 'Content-Type: application/json' \
--data-raw '{"type":"deposit", "destination":"100", "amount":110}'
```

Also you can use postman, or test it automatically at:  
https://ipkiss.pragmazero.com/
