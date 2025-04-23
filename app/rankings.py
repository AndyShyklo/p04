import os
import pandas as pd
from pymongo import MongoClient

dir_path = os.path.dirname(__file__)
with open(os.path.join(dir_path, "keys", "mongodb.txt"), "r") as f:
    key = f.read().strip()

client = MongoClient(key)

def make_ranking(username, country, ranking):
    db = client.get_database("ratings")
    col = db.get_collection("ratings")

    auth = check_if_ranking(username, country)

    print("started making", flush=True)
    print(auth, flush=True)

    if auth:
        col.insert_one({"username": username, "country": country, "ranking": ranking})
        return([True, None])
    else:
        print("Failed: Review completed already")
        return([False, "Failed: Review already completed"])

def check_if_ranking(username, country):
    db = client.get_database("ratings")
    col = db.get_collection("ratings")

    auth = col.find_one({"username": username, "country": country})
    print(auth, flush=True)

    if auth == None:
        return True
    else:
        return False

def calculate_rankings(country):
    db = client.get_database("ratings")
    col = db.get_collection("ratings")

    cur = col.find({"country": country}, {"ranking": 1, "_id": 0})

    total = 0
    i = 0

    for doc in cur:
        if "ranking" in doc:
            total += int(doc["ranking"])
            i += 1

    if (not (i == 0)):
        avg = total / i
    else:
        avg = 0

    return(round(avg, 2))

def num_rankings(country):
    db = client.get_database("ratings")
    col = db.get_collection("ratings")

    cur = col.find({"country": country}, {"ranking": 1, "_id": 0})

    print(cur, flush=True)
    print(type(cur), flush=True)

    i = 0

    for doc in cur:
        print(doc, flush=True)
        if "ranking" in doc:
            print(True, flush=True)
            i += 1

    print("i:", i, flush=True)

    return(i)

def get_rankings(username):
    db = client.get_database("ratings")
    col = db.get_collection("ratings")

    cur = col.find({"username": username}, {"country": 1, "ranking": 1, "_id": 0})

    docs = []

    for doc in cur:
        if "ranking" in doc:
            try:
                doc["ranking"] = int(doc["ranking"])
            except:
                doc["ranking"] = -1
        docs.append(doc)

    return(docs)
