import pandas as pd
import numpy as np
import datetime

datesNotAvailable = []

listingComparedDates = {}

costOfRentals = {}

mainData = pd.read_csv(r'C:\Users\karan.shah05\PycharmProjects\AirBnB vs Rental in Seattle\Data\AirbnbData\mainData.csv')

mainData['date'] = pd.to_datetime(mainData['date'], format='%Y-%m-%d')

dataForJan2016 = mainData[mainData.date.between('1/1/2016', '1/31/2016', inclusive=True)]

for index, rows in dataForJan2016.iterrows():
    if rows['listing_id'] not in costOfRentals.keys() & rows['available'] == 'f':
        costOfRentals[rows['listing_id']] = rows['price']

        if rows['listing_id'] not in listingComparedDates.keys():
            listingComparedDates[rows['listing_id']] = datesNotAvailable.append(rows['date'])
        if rows['listing_id'] in listingComparedDates.keys() & rows['date'] not in listingComparedDates.get(rows['listing_id']):
            listingComparedDates[rows['listing_id']] = datesNotAvailable.append(rows['date'])

    print(listingComparedDates)




