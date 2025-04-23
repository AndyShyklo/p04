import os
import pandas as pd
import colorsys
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

# find_diff()

# print(country_array)

def last_vals_score():
    ranks = {}

    for country in country_array:
        try:
            ranks[country] = float(get_happiness_score(2019, country))
        except:
            print("No year found 2019")
            try:
                print(country)
                ranks[country] = float(get_happiness_score(2018, country))
            except:
                print("No year found 2018")
                try:
                    print(country)
                    ranks[country] = float(get_happiness_score(2017, country))
                except:
                    print("No year found 2017")
                    try:
                        print(country)
                        ranks[country] = float(get_happiness_score(2016, country))
                    except:
                        print("No year found 2016")
                        try:
                            print(country)
                            ranks[country] = float(get_happiness_score(2015, country))
                        except:
                            print("No year found 2015 and at all")

    print(ranks)
    return(ranks)

ranks_dict = {'Afghanistan': 3.203, 'Albania': 4.719, 'Algeria': 5.211, 'Angola': 3.795, 'Argentina': 6.086, 'Armenia': 4.559, 'Australia': 7.228, 'Austria': 7.246, 'Azerbaijan': 5.208, 'Bahrain': 6.199, 'Bangladesh': 4.456, 'Belarus': 5.323, 'Belgium': 6.923, 'Belize': 5.956, 'Benin': 4.883, 'Bhutan': 5.082, 'Bolivia': 5.779, 'Bosnia and Herzegovina': 5.386, 'Botswana': 3.488, 'Brazil': 6.3, 'Bulgaria': 5.011, 'Burkina Faso': 4.587, 'Burundi': 3.775, 'Cambodia': 4.7, 'Cameroon': 5.044, 'Canada': 7.278, 'Central African Republic': 3.083, 'Chad': 4.35, 'Chile': 6.444, 'China': 5.191, 'Colombia': 6.125, 'Comoros': 3.973, 'Congo (Brazzaville)': 4.812, 'Congo (Kinshasa)': 4.418, 'Costa Rica': 7.167, 'Croatia': 5.432, 'Cyprus': 6.046, 'Czech Republic': 6.852, 'Denmark': 7.6, 'Djibouti': 4.369, 'Dominican Republic': 5.425, 'Ecuador': 6.028, 'Egypt': 4.166, 'El Salvador': 6.253, 'Estonia': 5.893, 'Ethiopia': 4.286, 'Finland': 7.769, 'France': 6.592, 'Gabon': 4.799, 'Gambia': 4.516, 'Georgia': 4.519, 'Germany': 6.985, 'Ghana': 4.996, 'Greece': 5.287, 'Guatemala': 6.436, 'Guinea': 4.534, 'Haiti': 3.597, 'Honduras': 5.86, 'Hong Kong': 5.43, 'Hungary': 5.758, 'Iceland': 7.494, 'India': 4.015, 'Indonesia': 5.192, 'Iran': 4.548, 'Iraq': 4.437, 'Ireland': 7.021, 'Israel': 7.139, 'Italy': 6.223, 'Ivory Coast': 4.944, 'Jamaica': 5.89, 'Japan': 5.886, 'Jordan': 4.906, 'Kazakhstan': 5.809, 'Kenya': 4.509, 'Kosovo': 6.1, 'Kuwait': 6.021, 'Kyrgyzstan': 5.261, 'Laos': 4.796, 'Latvia': 5.94, 'Lebanon': 5.197, 'Lesotho': 3.802, 'Liberia': 3.975, 'Libya': 5.525, 'Lithuania': 6.149, 'Luxembourg': 7.09, 'Madagascar': 3.933, 'Malawi': 3.41, 'Malaysia': 5.339, 'Mali': 4.39, 'Malta': 6.726, 'Mauritania': 4.49, 'Mauritius': 5.888, 'Mexico': 6.595, 'Moldova': 5.529, 'Mongolia': 5.285, 'Montenegro': 5.523, 'Morocco': 5.208, 'Mozambique': 4.466, 'Myanmar': 4.36, 'Namibia': 4.639, 'Nepal': 4.913, 'Netherlands': 7.488, 'New Zealand': 7.307, 'Nicaragua': 6.105, 'Niger': 4.628, 'Nigeria': 5.265, 'North Cyprus': 5.718, 'North Macedonia': 5.274, 'Norway': 7.554, 'Oman': 6.853, 'Pakistan': 5.653, 'Palestinian Territories': 4.696, 'Panama': 6.321, 'Paraguay': 5.743, 'Peru': 5.697, 'Philippines': 5.631, 'Poland': 6.182, 'Portugal': 5.693, 'Puerto Rico': 7.039, 'Qatar': 6.374, 'Romania': 6.07, 'Russia': 5.648, 'Rwanda': 3.334, 'Saudi Arabia': 6.375, 'Senegal': 4.681, 'Serbia': 5.603, 'Sierra Leone': 4.374, 'Singapore': 6.262, 'Slovakia': 6.198, 'Slovenia': 6.118, 'Somalia': 4.668, 'Somaliland': 5.057, 'South Africa': 4.722, 'South Korea': 5.895, 'South Sudan': 2.853, 'Spain': 6.354, 'Sri Lanka': 4.366, 'Sudan': 4.139, 'Suriname': 6.269, 'Swaziland': 4.212, 'Sweden': 7.343, 'Switzerland': 7.48, 'Syria': 3.462, 'Taiwan': 6.446, 'Tajikistan': 5.467, 'Tanzania': 3.231, 'Thailand': 6.008, 'Togo': 4.085, 'Trinidad and Tobago': 6.192, 'Tunisia': 4.461, 'Turkey': 5.373, 'Turkmenistan': 5.247, 'Uganda': 4.189, 'Ukraine': 4.332, 'United Arab Emirates': 6.825, 'United Kingdom': 7.054, 'United States': 6.892, 'Uruguay': 6.293, 'Uzbekistan': 6.174, 'Venezuela': 4.707, 'Vietnam': 5.175, 'Yemen': 3.38, 'Zambia': 4.107, 'Zimbabwe': 3.663}

def col_val():
    minV = 2
    maxV = 8
    ranks = ranks_dict
    color_dict = {}
    for key, value in ranks.items():
        cla = max(minV, min(maxV, value))
        rat = (cla - minV) / (maxV - minV)

        hue = 5 + rat * ((cla - 4) * 0.16)

        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)

        red = round(r*255)
        green = round(g*255)
        blue = round(b*255)
    
        color_dict[key] = "#{:02x}{:02x}{:02x}".format(red, green, blue)

    return(color_dict)

def get_abbreviations():
    country_names = {
    "AF": "Afghanistan",
    "AL": "Albania",
    "DZ": "Algeria",
    "AO": "Angola",
    "AR": "Argentina",
    "AM": "Armenia",
    "AU": "Australia",
    "AT": "Austria",
    "AZ": "Azerbaijan",
    "BH": "Bahrain",
    "BD": "Bangladesh",
    "BY": "Belarus",
    "BE": "Belgium",
    "BZ": "Belize",
    "BJ": "Benin",
    "BT": "Bhutan",
    "BO": "Bolivia",
    "BA": "Bosnia and Herzegovina",
    "BW": "Botswana",
    "BR": "Brazil",
    "BG": "Bulgaria",
    "BF": "Burkina Faso",
    "BI": "Burundi",
    "KH": "Cambodia",
    "CM": "Cameroon",
    "CA": "Canada",
    "CF": "Central African Republic",
    "TD": "Chad",
    "CL": "Chile",
    "CN": "China",
    "CO": "Colombia",
    "KM": "Comoros",
    "CG": "Congo (Brazzaville)",
    "CD": "Congo (Kinshasa)",
    "CR": "Costa Rica",
    "HR": "Croatia",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DK": "Denmark",
    "DJ": "Djibouti",
    "DO": "Dominican Republic",
    "EC": "Ecuador",
    "EG": "Egypt",
    "SV": "El Salvador",
    "EE": "Estonia",
    "ET": "Ethiopia",
    "FI": "Finland",
    "FR": "France",
    "GA": "Gabon",
    "GM": "Gambia",
    "GE": "Georgia",
    "DE": "Germany",
    "GH": "Ghana",
    "GR": "Greece",
    "GT": "Guatemala",
    "GN": "Guinea",
    "HT": "Haiti",
    "HN": "Honduras",
    "HK": "Hong Kong",
    "HU": "Hungary",
    "IS": "Iceland",
    "IN": "India",
    "ID": "Indonesia",
    "IR": "Iran",
    "IQ": "Iraq",
    "IE": "Ireland",
    "IL": "Israel",
    "IT": "Italy",
    "CI": "Ivory Coast",
    "JM": "Jamaica",
    "JP": "Japan",
    "JO": "Jordan",
    "KZ": "Kazakhstan",
    "KE": "Kenya",
    "XK": "Kosovo",
    "KW": "Kuwait",
    "KG": "Kyrgyzstan",
    "LA": "Laos",
    "LV": "Latvia",
    "LB": "Lebanon",
    "LS": "Lesotho",
    "LR": "Liberia",
    "LY": "Libya",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "MG": "Madagascar",
    "MW": "Malawi",
    "MY": "Malaysia",
    "ML": "Mali",
    "MT": "Malta",
    "MR": "Mauritania",
    "MU": "Mauritius",
    "MX": "Mexico",
    "MD": "Moldova",
    "MN": "Mongolia",
    "ME": "Montenegro",
    "MA": "Morocco",
    "MZ": "Mozambique",
    "MM": "Myanmar",
    "NA": "Namibia",
    "NP": "Nepal",
    "NL": "Netherlands",
    "NZ": "New Zealand",
    "NI": "Nicaragua",
    "NE": "Niger",
    "NG": "Nigeria",
    "MK": "North Macedonia",
    "NO": "Norway",
    "OM": "Oman",
    "PK": "Pakistan",
    "PS": "Palestinian Territories",
    "PA": "Panama",
    "PY": "Paraguay",
    "PE": "Peru",
    "PH": "Philippines",
    "PL": "Poland",
    "PT": "Portugal",
    "PR": "Puerto Rico",
    "QA": "Qatar",
    "RO": "Romania",
    "RU": "Russia",
    "RW": "Rwanda",
    "SA": "Saudi Arabia",
    "SN": "Senegal",
    "RS": "Serbia",
    "SL": "Sierra Leone",
    "SG": "Singapore",
    "SK": "Slovakia",
    "SI": "Slovenia",
    "SO": "Somalia",
    "ZA": "South Africa",
    "KR": "South Korea",
    "SS": "South Sudan",
    "ES": "Spain",
    "LK": "Sri Lanka",
    "SD": "Sudan",
    "SR": "Suriname",
    "SZ": "Swaziland",
    "SE": "Sweden",
    "CH": "Switzerland",
    "SY": "Syria",
    "TW": "Taiwan",
    "TJ": "Tajikistan",
    "TZ": "Tanzania",
    "TH": "Thailand",
    "TG": "Togo",
    "TT": "Trinidad and Tobago",
    "TN": "Tunisia",
    "TR": "Turkey",
    "TM": "Turkmenistan",
    "UG": "Uganda",
    "UA": "Ukraine",
    "AE": "United Arab Emirates",
    "GB": "United Kingdom",
    "US": "United States",
    "UY": "Uruguay",
    "UZ": "Uzbekistan",
    "VE": "Venezuela",
    "VN": "Vietnam",
    "YE": "Yemen",
    "ZM": "Zambia",
    "ZW": "Zimbabwe"
    }
    return country_names