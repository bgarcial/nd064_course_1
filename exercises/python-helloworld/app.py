import pytest
from flask import Flask
from flask import jsonify, json
# from flask_api import status
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


# @pytest.fixture
@app.route('/status')
def health_check():
    response = [
        {'user': 'admin'},
        {'result': 'OK - Healthy'}
    ]
    return jsonify(response)
    # return health_check, status.HTTP_200_OK

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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
