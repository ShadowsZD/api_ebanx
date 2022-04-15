import flask
from flask import request, jsonify, make_response
from model.event import Events

app = flask.Flask(__name__)
app.config["DEBUG"] = True

events = Events()

@app.route('/event', methods=['POST'])
def event_handler():
    data = request.get_json()
    resp = events.process_event(**data)

    return make_response(jsonify(resp[0]), resp[1])

@app.route('/reset', methods=['POST'])
def reset():
    
    return make_response(events.reset())

@app.route('/balance', methods=['GET'])
def balance():

    id = request.args.get("account_id")
    resp = events.get_balance(id)
    
    return make_response(str(resp[0]), resp[1])

app.run()
