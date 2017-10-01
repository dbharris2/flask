from flask import Flask
from mongo_json_encoder import MongoJSONEncoder
from pymongo import MongoClient
import os
import requests

app = Flask(__name__)

@app.route("/")
def joke():
    response = requests.get('http://api.icndb.com/jokes/random')
    json = response.json()
    joke = json['value']['joke']
    return joke

@app.route("/fitbit")
def fitbit():
    mongo_client = MongoClient(os.environ['MONGODB_URI'])
    db = mongo_client.fitbit_users
    results = {}
    for user in db.users.find():
      results[user['user_id']] = user
    return MongoJSONEncoder().encode(results)

if __name__ == "__main__":
    app.run()
