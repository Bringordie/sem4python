import pandas as pd
import numpy as np
import csv
import datetime
import datetime

start_year = 1995
end_year = 2021
difference = end_year - start_year

countries = ["Greece", "Spain", "France",
             "Italy", "Portugal", "European Union"]
categories = ["Strawberries", "Nectarines", "Apples Braeburn"]


test = it_nectaries[((it_nectaries[:]['Period']) >= 201901)
                    & ((it_nectaries[:]['Period']) <= 201912)]
test2 = el_nectaries[((el_nectaries[:]['Period']) >= 201901)
                     & ((el_nectaries[:]['Period']) <= 201912)]
test.iloc[:]["MP Market Price"].sum()

all_food_data = {}


for num, country in enumerate(countries, start=0):
    country_info = {}
    country_mask = all_info.get(country)
    all_food_data[country] = {}
    for category in categories:
        cat_country = pd.DataFrame(country_mask[category])
        all_food_data[country][category] = []
        if (len(cat_country) != 0):
            for years in range(difference):
                get_start = int(str(start_year+years)+"01")
                get_end = int(str(start_year+years)+"12")
                year_mask = cat_country[((cat_country[:]['Period']) >= get_start) & (
                    (cat_country[:]['Period']) <= get_end)]
                sum = year_mask.iloc[:]["MP Market Price"].sum()
                mean = sum / 12
                if (sum != 0):
                    all_food_data[countries[num]][category].append(
                        {"year": start_year+years, "avg. cost": mean})


df = pd.read_csv('data/market-prices-fruit-products_en_6.csv', skiprows=0)


county_codes = ["EL", "ES", "FR", "IT", "PT", "EU"]
countries = ["Greece", "Spain", "France",
             "Italy", "Portugal", "European Union"]
categories = ["Strawberries", "Nectarines", "Apples Braeburn"]


all_info = {}


for num, country in enumerate(county_codes, start=0):
    country_info = {}
    country_mask = (df[:]['Country'].str.contains(country) == True)
    data = df[country_mask].iloc[:, 39:-2]
    for category in categories:
        country_info[category] = df.loc[country_mask & (
            df[:]['Product desc'].str.contains(category))]
    all_info[countries[num]] = country_info


# all_info
countries = ["Greece", "Spain", "France",
             "Italy", "Portugal", "European Union"]
#countries = ["EL", "ES", "FR", "IT", "PT", "EU"]
categories = ["Strawberries", "Nectarines", "Apples Braeburn"]

all_food_data = {}

start_year = 1995
end_year = 2021
months = 12
difference = end_year - start_year

# For loop for each country
for num, country in enumerate(countries, start=0):
    country_info = {}
    country_mask = all_info.get(country)
    for category in categories:
        cat_country = pd.DataFrame(country_mask[category])
        if (len(cat_country) != 0):
            for years in range(difference):
                get_start = int(str(start_year+years)+"01")
                get_end = int(str(start_year+years)+"12")
                year_mask = cat_country[((cat_country[:]['Period']) >= get_start) & (
                    (cat_country[:]['Period']) <= get_end)]
                year_mask1 = cat_country[((cat_country[:]['Period']) >= 199501) & (
                    (cat_country[:]['Period']) <= 199512)]
                sum = year_mask.iloc[:]["MP Market Price"].sum()
                all_food_data[countries[num]] = {
                    "year": start_year+years, "avg. cost": sum}
