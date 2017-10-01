from flask import Flask
from mongo_json_encoder import MongoJSONEncoder
from pymongo import MongoClient
import os

app = Flask(__name__)

@app.route("/")
def hello():
    mongo_client = MongoClient(os.environ['MONGODB_URI'])
    db = mongo_client.fitbit_users
    results = {}
    for user in db.users.find():
      results[user['user_id']] = user
    return MongoJSONEncoder().encode(results)

if __name__ == "__main__":
    app.run()
