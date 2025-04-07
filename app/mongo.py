import os
import pandas as pd
from pymongo import MongoClient

csv_path = "static/years"

with open("keys/mongodb.txt", "r") as f:
    key = f.read().strip()

client = MongoClient(key)
db = client.get_database("years")

def init():
    for filename in os.listdir(csv_path):
        if filename.endswith(".csv"):

            filepath = os.path.join(csv_path, filename)
            df = pd.read_csv(filepath)

            rec = df.to_dict(orient='records')

            col_name = os.path.splitext(filename)[0]

            col = db.get_collection(col_name)

            col.delete_many({}) #may need to remove

            if rec:
                col.insert_many(rec)
                print(f"insert {len(rec)} recs into {col_name}")

    print("data inserted")

init()

def get_col(year):
    return (db[str(year)])

print("2017 stats:")
print(get_col(2017))

def get_country(year, country):
    col = get_col(year)
    result = col.find_one({"Country or region": country})
    return (result)

print("2017 stats for norway:")
print(get_country(2017, "Norway"))

def get_happiness_score(year, country):
    print(type(get_country(year, country)))
    return(get_country(year, country).get("Score"))

print("2017 stats for norway happiness score:")
print(get_happiness_score(2017, "Norway"))

def get_happiness_rank(year, country):
    return(get_country(year, country).get("Overall rank"))

print("2017 stats for norway happiness rank:")
print(get_happiness_score(2017, "Norway"))

def get_gdp_capita(year, country):
    return(get_country(year, country).get("GDP per capita"))

print("2017 stats for norway gdp per capita:")
print(get_happiness_score(2017, "Norway"))
