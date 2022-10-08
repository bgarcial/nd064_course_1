from flask import Flask
from flask import jsonify
# from flask_api import status
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/status')
def health_check():
    health_check = {'result': 'OK - Healthy'}
    profile = {'user' : 'admin'}
    return jsonify(profile,health_check)
    # return health_check, status.HTTP_200_OK

@app.route('/metrics', methods=['GET'])
def metrics():

    response = [
        {'user' : 'admin'},
        'data: { UserCount: 140, UserCountActive: 23}'
    ]
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
