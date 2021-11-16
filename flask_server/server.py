import flask
import requests

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def handle_call():
    return "Successfully Connected"

@app.route('/getfact', methods=['GET'])
def get_fact():
    return "Hey!! I'm the fact you got!!!"

@app.route('/getname/<name>', methods=['POST'])
def extract_name(name):
    return "I got your name "+name;


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
