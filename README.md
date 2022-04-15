# api_ebanx
Simple api for test on ebanx

How to use it:

pip install flask on your environment

on bash:

export FLASK_APP=hello
flask run

or

python api/api.py

you can test the api using sending request on curl such as:
curl --location --request POST 'http://127.0.0.1:5000/event' \
--header 'Content-Type: application/json' \
--data-raw '{"type":"deposit", "destination":"100", "amount":110}'

also you can use postman, or test it automatically at: 
https://ipkiss.pragmazero.com/