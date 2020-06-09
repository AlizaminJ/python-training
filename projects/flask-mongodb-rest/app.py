from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

from bson.json_util import dumps #to convert bson tojson
from bson.objectid import ObjectId #to create objectID in MongoDB
from werkzeug.security import generate_password_hash, check_password_hash # hashing algo


app=Flask(__name__)
app.secret_key="secretkey"
app.config['MONGO_URI']="mongodb://localhost:27017/test"

mongo=PyMongo(app) #connect app tp DB

@app.route('/add', methods=['POST'])
def add_user():
  _json=request.json
  _name=_json['name']
  _email=_json['email']
  _password=_json['pwd']

  if _name and _email and _password and request.method=='POST':
    _hashed_password=generate_password_hash(_password)
    id=mongo.db.user.insert({'name':_name, 'email':_email, 'pwd':_hashed_password})

if __name__=="__main__":
  app.run(debug=True)