from flask import Flask
import os
import pymongo


# app = Flask(__name__)
DB_NAME = "Leftovers"
CLIENT  = "mongodb://localhost:27017/"


def signup(email,no,id,address):
    client = pymongo.MongoClient(CLIENT)
    db = client[DB_NAME]
    col = db["Users"]
    points = 100
    dict = { "Email": email, "Contact Number": no , "Address": address, "Points": points}

def connect():
    client = pymongo.MongoClient(CLIENT)
    db = client[DB_NAME]
    col = db["Users"]
    dict = { "name": "John", "address": "Highway 37" }

    x = col.insert_one(dict)

    print(client.list_database_names())

connect()

@app.route('/test')
def test():
    return "Connected to API Sucessfully!"


