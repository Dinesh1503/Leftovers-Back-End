from flask import Flask,request
from flask_cors import CORS
import os
import pymongo
import json

DB_NAME = "Leftovers"
CLIENT  = "mongodb://localhost:27017/"

def signup(email,no,address):
    client = pymongo.MongoClient(CLIENT)
    db = client[DB_NAME]
    col = db["Users"]
    points = 100
    dict = { "Email": email, "Contact Number": no , "Address": address, "Points": points}
    x = col.insert_one(dict)
    return "User Registered"

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
    return "Food Collected"


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
    if(not bool(output)):
        return "No food available that matches criteria"
    col.delete_one(output)
    print(json.dumps(output))
    return json.dumps(output)

def getuserinfo(email):
    client = pymongo.MongoClient(CLIENT)
    db = client[DB_NAME]
    col = db["Users"]
    query = {"Email":email}
    doc = col.find(query)
    output = {}
    for x in doc:
        output['email']=x['Email']
        output['no']=x['Contact Number']
        output['address']=x['Address']
        output['points']=x['Points']
    if(not bool(output)):
        return "User not registered in system"
    return json.dumps(output)

 
# signup("yahoo.com","08","Leeds")
# give("cereals","Today","NonCooked","Veg","gmail.com")
# match("NonCooked","Veg")

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "{'status':'Alive'}"
 
@app.route('/api/signup',methods=["POST"])
def getdata():
    # if(request.args.get['email']):
    email = request.args.get('email')
    no = request.args.get('no')
    address = request.args.get('address')
    return signup(email,no,address)

@app.route('/api/donate',methods=["POST"])
def donate():
    email = request.args.get('email')
    food = request.args.get('food')
    expiry = request.args.get('expiry')
    type = request.args.get('type')
    diet = request.args.get('diet')
    return give(food,expiry,type,diet,email)

@app.route('/api/order',methods=["POST"])
def order():
    type = request.args.get('type')
    diet = request.args.get('diet')
    return match(type,diet)


@app.route('/api/userinfo',methods=["GET"])
def userinfo():
    email = request.args.get('email')
    return getuserinfo(email)

if __name__ == '__main__':
    app.run(host="localhost", port=4123, debug=True)