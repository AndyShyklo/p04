import os
import pandas as pd
from pymongo import MongoClient

csv_path = "static/years"

def get_db():
	dir_path = os.path.dirname(__file__)
	with open(os.path.join(dir_path, "keys", "mongodb.txt"), "r") as f:
    		key = f.read().strip()

	client = MongoClient(key)
	db = client.get_database("years")
	return(db)

years = [2015, 2016, 2017, 2018, 2019]

def init():
    db = get_db()
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
    db = get_db()
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
    if country_exists(country):
        dict_res = {}
        for year in years:
            try:
                a = get_happiness_score(year, country)
                dict_res[year] = a
            except:
                print(f"couldnt add data for {year} and {country} happiness score")
        return(dict_res)

# print("happiness score stat for all years norway")
# print(get_happiness_score_yearly("Norway"))

def get_happiness_rank_yearly(country):
    if country_exists(country):
        dict_res = {}
        for year in years:
            try:
                a = get_happiness_rank(year, country)
                dict_res[year] = a
            except:
                print(f"couldnt add data for {year} and {country} happiness rank")
        return(dict_res)

# print("happiness rank stat for all years norway")
# print(get_happiness_rank_yearly("Norway"))

def get_gdp_per_capita_yearly(country):
    if country_exists(country):
        dict_res = {}
        for year in years:
            try:
                a = get_gdp_capita(year, country)
                dict_res[year] = a
            except:
                print(f"couldnt add data for {year} and {country} gdp per capita")
        return(dict_res)

# print("gdp per capita stat for all years norway")
# print(get_gdp_per_capita_yearly("Norway"))

def get_health_yearly(country):
    if country_exists(country):
        dict_res = {}
        for year in years:
            try:
                a = get_health(year, country)
                dict_res[year] = a
            except:
                print(f"couldnt add data for {year} and {country} health")
        return(dict_res)

# print("health stat for all years norway")
# print(get_health_yearly("Norway"))

def get_family_yearly(country):
    if country_exists(country):
        dict_res = {}
        for year in years:
            try:
                a = get_family(year, country)
                dict_res[year] = a
            except:
                print(f"couldnt add data for {year} and {country} family")
        return(dict_res)

# print("family stat for all years norway")
# print(get_family_yearly("Norway"))

def get_freedom_yearly(country):
    if country_exists(country):
        dict_res = {}
        for year in years:
            try:
                a = get_freedom(year, country)
                dict_res[year] = a
            except:
                print(f"couldnt add data for {year} and {country} freedom")
        return(dict_res)

# print("freedom stat for all years norway")
# print(get_freedom_yearly("Norway"))

def get_generosity_yearly(country):
    if country_exists(country):
        dict_res = {}
        for year in years:
            try:
                a = get_generosity(year, country)
                dict_res[year] = a
            except:
                print(f"couldnt add data for {year} and {country} generosity")
        return(dict_res)

# print("generosity stat for all years norway")
# print(get_generosity_yearly("Norway"))

def get_gov_trust_yearly(country):
    if country_exists(country):
        dict_res = {}
        for year in years:
            try:
                a = get_gov_trust(year, country)
                dict_res[year] = a
            except:
                print(f"couldnt add data for {year} and {country} gov trust")
        return(dict_res)

# print("gov trust stat for all years norway")
# print(get_gov_trust_yearly("Norway"))

def get_countries():
    arr = []
    for year in years:
        col = get_col(year)
        if (year > 2014 and year < 2018):
            cur = col.find({}, {"Country": 1, "_id": 0})
        else:
            cur = col.find({}, {"Country or region": 1, "_id": 0})
        # print(cur)
        for a in cur:
            if (year > 2014 and year < 2018):
                b = a.get("Country")
                if b not in arr:
                    arr.append(b)
            else:
                b = a.get("Country or region")
                if b not in arr:
                    arr.append(b)
    # print(arr)
    # print(len(arr))
    arr.sort()
    # print(arr)
    return(arr)

country_array = get_countries()

def country_exists(country):
    if country in country_array:
        return True
    else:
        return False

def find_diff():
    countryList = ['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Estonia', 'Ethiopia', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Cyprus', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palestinian Territories', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'Somaliland', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

    listErr = [c for c in countryList if c not in country_array]
    arrayErr = [c for c in country_array if c not in countryList]

    print(listErr)
    print(arrayErr)

find_diff()

print(country_array)
