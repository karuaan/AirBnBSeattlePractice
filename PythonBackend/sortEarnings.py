import pandas as pd
import pprint as pp
import pickle

listingComparedDates = dict()

costOfRentals = dict()

datesNotAvailable = list()

dailyPriceArray = list()

mainData = pd.read_csv(r'C:\Users\karan.shah05\PycharmProjects\AirBnB vs Rental in Seattle\Data\AirbnbData\mainData.csv')

mainData['date'] = pd.to_datetime(mainData['date'], format='%Y-%m-%d')

breakDataByMonths = [g for n, g in mainData.groupby(pd.Grouper(key='date', freq='Y'))]

dataForJan2016 = mainData[mainData.date.between('2016-01-01', '2016-01-31', inclusive=True)]

dataForJan2016.to_csv(r'C:\Users\karan.shah05\PycharmProjects\AirBnB vs Rental in Seattle\Data\AirbnbData\Jan2016.csv')

for index, row in dataForJan2016.iterrows():
    listing_id = row['listing_id']
    availability = row['available']

    if listing_id not in listingComparedDates and availability == "f":
        datesNotAvailable = list()
        dailyPriceArray = list()

        datesNotAvailable.append(row['date'])
        dailyPriceArray.append(row['price'])

        listingComparedDates[listing_id] = datesNotAvailable
        costOfRentals[listing_id] = dailyPriceArray

    else:
        if listing_id in listingComparedDates and availability == "f":
            datesNotAvailable.append(row['date'])
            dailyPriceArray.append(row['price'])
            datesNotAvailable = listingComparedDates[listing_id]
            dailyPriceArray = costOfRentals[listing_id]

for key, value in costOfRentals.items():
    newFloatArray = list()
    for i in value:
        newValueWithoutDollar = i.replace('$', '')
        newValue = newValueWithoutDollar.replace(',', '')
        newValue = float(newValue)
        newFloatArray.append(newValue)
    costOfRentals[key] = newFloatArray

listingWithAvgPrice = dict()

for key, value in costOfRentals.items():
    avgDailyPrice = sum(value)/len(value)
    avgDailyPrice = round(avgDailyPrice, 2)
    listingWithAvgPrice[key] = avgDailyPrice




