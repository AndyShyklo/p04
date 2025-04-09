import os
import pandas as pd
from pymongo import MongoClient

csv_path = "static/years"

with open("keys/mongodb.txt", "r") as f:
    key = f.read().strip()

client = MongoClient(key)
db = client.get_database("years")

years = [2015, 2016, 2017, 2018, 2019]

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

#init()

def get_col(year):
    return (db[str(year)])

# print("2017 stats:")
# print(get_col(2017))

def get_country(year, country):
    col = get_col(year)
    if (year > 2014 and year < 2018):
        result = col.find_one({"Country": country})
    elif (year > 2017 and year < 2020):
        result = col.find_one({"Country or region": country})
    return (result)

# print("2017 stats for norway:")
# print(get_country(2017, "Norway"))

def get_happiness_score(year, country):
    res = get_country(year, country)
    if (year > 2014 and year < 2017):
        result = res.get("Happiness Score")
    elif (year == 2017):
        result = res.get("Happiness.Score")
    elif (year > 2017 and year < 2020):
        result = res.get("Score")
    else:
        result = "Error"
    return(result)

# print("2017 stats for norway happiness score:")
# print(get_happiness_score(2017, "Norway"))

def get_happiness_rank(year, country):
    res = get_country(year, country)
    if (year > 2014 and year < 2017):
        result = res.get("Happiness Rank")
    elif (year == 2017):
        result = res.get("Happiness.Rank")
    elif (year > 2017 and year < 2020):
        result = res.get("Overall rank")
    else:
        result = "Error"
    return(result)

# print("2017 stats for norway happiness rank:")
# print(get_happiness_rank(2017, "Norway"))

def get_gdp_capita(year, country):
    res = get_country(year, country)
    if (year > 2014 and year < 2017):
        result = res.get("Economy (GDP per Capita)")
    elif (year == 2017):
        result = res.get("Economy..GDP.per.Capita.")
    elif (year > 2017 and year < 2020):
        result = res.get("GDP per capita")
    else:
        result = "Error"
    return(result)

# print("2017 stats for norway gdp per capita:")
# print(get_gdp_capita(2017, "Norway"))

def get_health(year, country):
    res = get_country(year, country)
    if (year > 2014 and year < 2017):
        result = res.get("Health (Life Expectancy)")
    elif (year == 2017):
        result = res.get("Health..Life.Expectancy.")
    elif (year > 2017 and year < 2020):
        result = res.get("Healthy life expectancy")
    else:
        result = "Error"
    return(result)

# print("2017 stats for norway health life expectancy:")
# print(get_health(2017, "Norway"))

def get_family(year, country):
    res = get_country(year, country)
    if (year > 2014 and year < 2018):
        result = res.get("Family")
    elif (year > 2017 and year < 2020):
        result = res.get("Social support")
    else:
        result = "Error"
    return(result)

# print("2017 stats for norway family:")
# print(get_family(2017, "Norway"))

def get_freedom(year, country):
    res = get_country(year, country)
    if (year > 2014 and year < 2018):
        result = res.get("Freedom")
    elif (year > 2017 and year < 2020):
        result = res.get("Freedom to make life choices")
    else:
        result = "Error"
    return(result)

# print("2017 stats for norway freedom:")
# print(get_freedom(2017, "Norway"))

def get_gov_trust(year, country):
    res = get_country(year, country)
    if (year > 2014 and year < 2017):
        result = res.get("Trust (Government Corruption)")
    elif (year == 2017):
        result = res.get("Trust..Government.Corruption.")
    elif (year > 2017 and year < 2020):
        result = res.get("Perceptions of corruption")
    else:
        result = "Error"
    return(result)

# print("2017 stats for norway trust and gov corruption:")
# print(get_gov_trust(2017, "Norway"))

def get_generosity(year, country):
    res = get_country(year, country)
    if (year > 2014 and year < 2020):
        result = res.get("Generosity")
    else:
        result = "Error"
    return(result)

# print("2017 stats for norway generosity:")
# print(get_generosity(2017, "Norway"))

def get_yearly(country):
    dict_res = {}
    for year in years:
        dict_res[year] = get_country(year, country)
    return(dict_res)

# print("all stats for all years norway")
# print(get_yearly("Norway"))

def get_happiness_score_yearly(country):
    dict_res = {}
    for year in years:
        dict_res[year] = get_happiness_score(year, country)
    return(dict_res)

# print("happiness score stat for all years norway")
# print(get_happiness_score_yearly("Norway"))

def get_happiness_rank_yearly(country):
    dict_res = {}
    for year in years:
        dict_res[year] = get_happiness_rank(year, country)
    return(dict_res)

# print("happiness rank stat for all years norway")
# print(get_happiness_rank_yearly("Norway"))

def get_gdp_per_capita_yearly(country):
    dict_res = {}
    for year in years:
        dict_res[year] = get_gdp_capita(year, country)
    return(dict_res)

# print("gdp per capita stat for all years norway")
# print(get_gdp_per_capita_yearly("Norway"))

def get_health_yearly(country):
    dict_res = {}
    for year in years:
        dict_res[year] = get_health(year, country)
    return(dict_res)

# print("health stat for all years norway")
# print(get_health_yearly("Norway"))

def get_family_yearly(country):
    dict_res = {}
    for year in years:
        dict_res[year] = get_family(year, country)
    return(dict_res)

# print("family stat for all years norway")
# print(get_family_yearly("Norway"))

def get_freedom_yearly(country):
    dict_res = {}
    for year in years:
        dict_res[year] = get_freedom(year, country)
    return(dict_res)

# print("freedom stat for all years norway")
# print(get_freedom_yearly("Norway"))

def get_generosity_yearly(country):
    dict_res = {}
    for year in years:
        dict_res[year] = get_generosity(year, country)
    return(dict_res)

# print("generosity stat for all years norway")
# print(get_generosity_yearly("Norway"))

def get_gov_trust_yearly(country):
    dict_res = {}
    for year in years:
        dict_res[year] = get_gov_trust(year, country)
    return(dict_res)

# print("gov trust stat for all years norway")
# print(get_gov_trust_yearly("Norway"))
