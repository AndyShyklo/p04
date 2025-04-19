import os
import pandas as pd
from pymongo import MongoClient

dir_path = os.path.dirname(__file__)
with open(os.path.join(dir_path, "keys", "mongodb.txt"), "r") as f:
    key = f.read().strip()

client = MongoClient(key)

def auth_user(username, password):
    db = client.get_database("users")
    col = db.get_collection("users")

    auth = col.find_one({"username": username, "password": password})

    print(auth)

    if auth == None:
        print("Invalid login")
        return([False, "Invalid login"])
    else:
        return([True, None])

def make_user(username, password):
    db = client.get_database("users")
    col = db.get_collection("users")

    auth = col.find_one({"username": username})

    print(auth)

    if auth == None:
        col.insert_one({"username": username, "password": password})
        return([True, None])
    else:
        print("Username Taken")
        return([False, "Username Taken"])
