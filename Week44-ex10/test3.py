import pandas as pd
import numpy as np
import csv
import datetime

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

start_year = 1995
end_year = 2021
difference = end_year - start_year

countries = ["Greece", "Spain", "France",
             "Italy", "Portugal", "European Union"]
categories = ["Strawberries", "Nectarines", "Apples Braeburn"]


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

all_food_data

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

countries = ["Greece", "Spain", "France",
             "Italy", "Portugal", "European Union"]
categories = ["Strawberries", "Nectarines", "Apples Braeburn"]

type(all_food_data)
df_data = pd.DataFrame(all_food_data)
df_data.head()
greece_df = all_food_data.get("Greece")
# spain_df
# france_df
# italy_df
# portugal_df
# eu_df
# greece_df

# def create_dataframes():

#df = pd.DataFrame (greece_df, columns = ['Strawberries','Nectarines','Apples Braeburn'])
test = greece_df.get('Nectarines')
test
# df = pd.DataFrame(test)
# plt.figure(1)
# plt.plot(df['year'], df['avg. cost'], 'k-')

list_df = {}
final_df = []
for num, country in enumerate(countries, start=0):
    list_df[country] = {}
    data = all_food_data.get(country)
    for category in categories:
        #list_df[country][category] = []
        if(data.get(category) is not None):
            if(len(data.get(category)) == 0):
                data.pop(category)
            else:
                list_df[country][category] = []
                # list_df[country][category].extend(data.get(category))
                list_df[country][category] = data.get(category)

print(list_df)
