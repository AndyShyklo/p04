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
        print(cur)
        for a in cur:
            if (year > 2014 and year < 2018):
                b = a.get("Country")
                if b not in arr:
                    arr.append(b)
            else:
                b = a.get("Country or region")
                if b not in arr:
                    arr.append(b)
    print(arr)
    print(len(arr))
    arr.sort()
    print(arr)
    return(arr)

country_array = get_countries()

def country_exists(country):
    if country in country_array:
        return True
    else:
        return False

def find_diff():
    countryList = [
        "Afghanistan",
        "Åland Islands",
        "Albania",
        "Algeria",
        "American Samoa",
        "Andorra",
        "Angola",
        "Anguilla",
        "Antarctica",
        "Antigua and Barbuda",
        "Argentina",
        "Armenia",
        "Aruba",
        "Australia",
        "Austria",
        "Azerbaijan",
        "Bahamas (the)",
        "Bahrain",
        "Bangladesh",
        "Barbados",
        "Belarus",
        "Belgium",
        "Belize",
        "Benin",
        "Bermuda",
        "Bhutan",
        "Bolivia",
        "Bonaire, Sint Eustatius and Saba",
        "Bosnia and Herzegovina",
        "Botswana",
        "Bouvet Island",
        "Brazil",
        "British Indian Ocean Territory (the)",
        "Brunei Darussalam",
        "Bulgaria",
        "Burkina Faso",
        "Burundi",
        "Cabo Verde",
        "Cambodia",
        "Cameroon",
        "Canada",
        "Cayman Islands (the)",
        "Central African Republic",
        "Chad",
        "Chile",
        "China",
        "Christmas Island",
        "Cocos (Keeling) Islands (the)",
        "Colombia",
        "Comoros",
        "Congo (Brazzaville)",
        "Congo (Kinshasa)",
        "Cook Islands (the)",
        "Costa Rica",
        "Croatia",
        "Cuba",
        "Curaçao",
        "Cyprus",
        "Czech Republic",
        "Ivory Coast",
        "Denmark",
        "Djibouti",
        "Dominica",
        "Dominican Republic",
        "Ecuador",
        "Egypt",
        "El Salvador",
        "Equatorial Guinea",
        "Eritrea",
        "Estonia",
        "Swaziland",
        "Ethiopia",
        "Falkland Islands (the) [Malvinas]",
        "Faroe Islands (the)",
        "Fiji",
        "Finland",
        "France",
        "French Guiana",
        "French Polynesia",
        "French Southern Territories (the)",
        "Gabon",
        "Gambia",
        "Georgia",
        "Germany",
        "Ghana",
        "Gibraltar",
        "Greece",
        "Greenland",
        "Grenada",
        "Guadeloupe",
        "Guam",
        "Guatemala",
        "Guernsey",
        "Guinea",
        "Guinea-Bissau",
        "Guyana",
        "Haiti",
        "Heard Island and McDonald Islands",
        "Holy See (the)",
        "Honduras",
        "Hong Kong",
        "Hungary",
        "Iceland",
        "India",
        "Indonesia",
        "Iran",
        "Iraq",
        "Ireland",
        "Isle of Man",
        "Israel",
        "Italy",
        "Jamaica",
        "Japan",
        "Jersey",
        "Jordan",
        "Kazakhstan",
        "Kenya",
        "Kiribati",
        "North Korea",
        "South Korea",
        "Kuwait",
        "Kyrgyzstan",
        "Laos",
        "Latvia",
        "Lebanon",
        "Lesotho",
        "Liberia",
        "Libya",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Macao",
        "Madagascar",
        "Malawi",
        "Malaysia",
        "Maldives",
        "Mali",
        "Malta",
        "Marshall Islands (the)",
        "Martinique",
        "Mauritania",
        "Mauritius",
        "Mayotte",
        "Mexico",
        "Micronesia (Federated States of)",
        "Moldova",
        "Monaco",
        "Mongolia",
        "Montenegro",
        "Montserrat",
        "Morocco",
        "Mozambique",
        "Myanmar",
        "Namibia",
        "Nauru",
        "Nepal",
        "Netherlands",
        "New Caledonia",
        "New Zealand",
        "Nicaragua",
        "Niger",
        "Nigeria",
        "Niue",
        "Norfolk Island",
        "Northern Mariana Islands (the)",
        "Norway",
        "Oman",
        "Pakistan",
        "Palau",
        "Palestinian Territories",
        "Panama",
        "Papua New Guinea",
        "Paraguay",
        "Peru",
        "Philippines",
        "Pitcairn",
        "Poland",
        "Portugal",
        "Puerto Rico",
        "Qatar",
        "North Macedonia",
        "Romania",
        "Russia",
        "Rwanda",
        "Réunion",
        "Saint Barthélemy",
        "Saint Helena, Ascension and Tristan da Cunha",
        "Saint Kitts and Nevis",
        "Saint Lucia",
        "Saint Martin (French part)",
        "Saint Pierre and Miquelon",
        "Saint Vincent and the Grenadines",
        "Samoa",
        "San Marino",
        "Sao Tome and Principe",
        "Saudi Arabia",
        "Senegal",
        "Serbia",
        "Seychelles",
        "Sierra Leone",
        "Singapore",
        "Sint Maarten (Dutch part)",
        "Slovakia",
        "Slovenia",
        "Solomon Islands",
        "Somalia",
        "South Africa",
        "South Georgia and the South Sandwich Islands",
        "South Sudan",
        "Spain",
        "Sri Lanka",
        "Sudan",
        "Suriname",
        "Svalbard and Jan Mayen",
        "Sweden",
        "Switzerland",
        "Syria",
        "Taiwan",
        "Tajikistan",
        "Tanzania",
        "Thailand",
        "Timor-Leste",
        "Togo",
        "Tokelau",
        "Tonga",
        "Trinidad and Tobago",
        "Tunisia",
        "Turkey",
        "Turkmenistan",
        "Turks and Caicos Islands (the)",
        "Tuvalu",
        "Uganda",
        "Ukraine",
        "United Arab Emirates",
        "United Kingdom",
        "United States Minor Outlying Islands (the)",
        "United States",
        "Uruguay",
        "Uzbekistan",
        "Vanuatu",
        "Venezuela",
        "Vietnam",
        "Virgin Islands (British)",
        "Virgin Islands (U.S.)",
        "Wallis and Futuna",
        "Western Sahara",
        "Yemen",
        "Zambia",
        "Zimbabwe"]
    print(countryList)
    arr = country_array
    for a in countryList:
        if a in country_array:
            countryList.remove(a)
            arr.remove(a)
    print(countryList)
    print(arr)

find_diff()
