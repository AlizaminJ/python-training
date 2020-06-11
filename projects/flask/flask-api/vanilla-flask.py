from flask import Flask, jsonify, request
app = Flask(__name__)

# @app.route('/')
# def index():
#   return jsonify( {'about': "Hello, world!"})


@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        some_json = request.get_json(force=True)
        return jsonify({'you sent': some_json}), 201
    else:
        return jsonify({'about': 'Hello there!'})


@app.route('/multi/<int:num>',  methods=['GET'])
def get_multiply_10(num):
    return jsonify({'result': num*10})


# flask
# EXPORT FLASK_APP=main.py
# EXPORT FLASK_DEBUG=1
# flask run

if __name__ == '__main__':
    app.run(debug=True)


# curl -H "Content-Type: application/json" -X POST -d '{"name":"abc", "address":"some address"}' http://127.0.0.1:5000/
# curl http://127.0.0.1:5000/multi/11