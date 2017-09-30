from bson import ObjectId
from flask import Flask, jsonify
from pymongo import MongoClient
import json
import os
import urllib

app = Flask(__name__)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@app.route("/")
def hello():
    mongo_client = MongoClient(os.environ['MONGODB_URI'])
    db = mongo_client.fitbit_users
    results = {}
    for user in db.users.find():
      results[user['user_id']] = user
    return JSONEncoder().encode(results)

if __name__ == "__main__":
    app.run()
