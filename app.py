from flask import Flask
import os
import pymongo
import json

# app = Flask(__name__)
DB_NAME = "Leftovers"
CLIENT  = "mongodb://localhost:27017/"


def signup(email,no,address):
    client = pymongo.MongoClient(CLIENT)
    db = client[DB_NAME]
    col = db["Users"]
    points = 100
    dict = { "Email": email, "Contact Number": no , "Address": address, "Points": points}
    x = col.insert_one(dict)

def give(food,expiry,type,diet,email):
    client = pymongo.MongoClient(CLIENT)
    db = client[DB_NAME]
    col = db["Stock"]
    data = {"Food":food,"Type":type,"Diet":diet,"Expiry":expiry}
    x = col.insert_one(data)


    client = pymongo.MongoClient(CLIENT)
    db = client[DB_NAME]
    col = db["Users"]
    query = {"Email":email}
    doc = col.find(query)
    for x in doc:
        p = x['Points']
    new_points = p + 10
    query = {"Points":p}
    newvalues = { "$set": { "Points":new_points} }
    col.update_one(query,newvalues)


def match(type,diet):
    client = pymongo.MongoClient(CLIENT)
    db = client[DB_NAME]
    col = db["Stock"]

    query = {"Type":type,"Diet":diet}
    doc = col.find(query)
    
    output = {}
    for x in doc:
        output['Food'] = x['Food']
        output['Type'] = x['Type']
        output['Diet'] = x['Diet']
        output['Expiry'] = x['Expiry']
    # print(output)
    print(json.dumps(output))
    return json.dumps(output)
        # if(x[0] ) 


# signup("yahoo.com","08","Leeds")
# give("cereals","Today","NonCooked","Veg","gmail.com")
match("NonCooked","Veg")





