import pandas as pd
import numpy as np
import csv

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
categories = ["Strawberries", "Nectarines", "Apples Braeburn"]

food_info = {}


for random, country in enumerate(countries, start=0):
    country_info = {}
    country_data = all_info.get(country)
    #data = df[country_mask].iloc[:,39:-2]
    for category in categories:
        data_category = country_data.get(category)
        if (len(data_category) == 0):
            print('DataFrame is empty!')
            break
        previous_year = 0
        years_price = 0
        counter = 0
        food_data = {}
        for idx, food in enumerate(data_category.iterrows(), start=0):
            counter = counter+1
            # Skipping header
            if (idx+1 > 10):
                year_get = food[1]["Period"]
                year = str(year_get.iloc[0])
                price_get = food[1]["MP Market Price"]
                price = price_get.iloc[0]
                if (previous_year == int(year[0:4]) & idx != 0):
                    years_price = years_price+int(price)

                if (previous_year != int(year[0:4]) & idx != 0):
                    average_price = years_price/(counter-1)
                    food_data[category] = {previous_year: average_price}
                    counter = 1
                    previous_year = int(year[0:4])

                food_info[countries[idx]] = food_data
