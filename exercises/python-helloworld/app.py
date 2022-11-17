import pytest
import ipdb
from flask import Flask
from flask import jsonify, json
# from flask_api import status
app = Flask(__name__)


@app.route('/status')
def health_check():
    response = [
        {'user': 'admin'},
        {'result': 'OK - Healthy'}
    ]
    ipdb.set_trace()
    
    return jsonify(response)


@app.route('/metrics', methods=['GET'])
def metrics():

    response = app.response_class(
        response=json.dumps({
            'status':'success',
            'code': 0,
            'data': {
                'UserCount': 140,
                'UserCountActive': 23
            }
        }),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route("/")
def hello():
    return "Hello World!"
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')
