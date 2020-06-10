# pip install Flask-PyMongo
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps  # to convert bson to json


app = Flask(__name__)
#app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'

mongo = PyMongo(app)


@app.route('/')
def index():
    return ('hello there')


@app.route('/stars', methods=['GET'])
def get_all_stars():
    stars = mongo.db.stars.find()
    resp = dumps(stars)
    # for s in star.find():
    #     output.append({'name': s['name'], 'distance': s['distance']})
    return jsonify({'output': resp})


@app.route('/star/<name>', methods=['GET'])
def get_one_star(name):
    star = mongo.db.stars
    s = star.find_one({'name': name})
    if s:
        output = {'name': s['name'], 'distance': s['distance']}
    else:
        output = "No such name"
    return jsonify({'result': output})


@app.route('/star', methods=['POST'])
def add_star():
    _json = request.json
    _name = _json['name']
    _distance = _json['distance']
    star_id = mongo.db.stars.insert({'name': _name, 'distance': _distance})
    new_star = mongo.db.stars.find_one({'_id': star_id})
    #output = {'name': new_star[name], 'distance': new_star['distance']}
    output = dumps(new_star)
    #output.status_code = 200
    resp = jsonify({'User added successfully': output})
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run(debug=True)
