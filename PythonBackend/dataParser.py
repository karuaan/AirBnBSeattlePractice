import pandas as pd
import pprint as pp

# Import Main Data
mainData = pd.read_csv(r'C:\Users\karan.shah05\PycharmProjects\AirBnB vs Rental in Seattle\Data\AirbnbData\mainData.csv')

# Sort Data According to Listing_id

mainData['date'] = pd.to_datetime(mainData['date'], format='%Y-%m-%d')

listing_ids = mainData['listing_id'].unique().tolist()

listOfMonths = mainData['date'].dt.month.unique().tolist()

listOfYears = mainData['date'].dt.year.unique().tolist()

# Get Separate Dataset by Listing Id
def sortDataByListingId(listing):
    mask = mainData['listing_id'] == listing
    newDataset = mainData[mask]

    return newDataset

# Get Yearly data for listing id
def sortDataByListingIdByYear(listing, year):
    dataset = sortDataByListingId(listing)
    mask = dataset['date'].dt.year == year
    newDataset = dataset[mask]

    return newDataset

# Get Data for a certain Listing Id by Month and year
def sortMonthlyDataByListingId(listing, year, month):
    dataset = sortDataByListingIdByYear(listing, year)
    mask = dataset['date'].dt.month == month
    newDataset = dataset[mask]

    return newDataset

# Display Data for all but Listing Id
def sortDataButListingId(listing):
    mask = mainData['listing_id'] == listing
    newDataset = mainData[~mask]

    return newDataset

# How Often Listing is booked in overall data
def sortDataByListingIdBooked(listing):
    dataset = sortDataByListingId(listing)
    mask = dataset['available'] == 'f'
    newDataset = dataset[mask]

    return newDataset

#How Often Listing is booked in Year
def sortDataByListingIdBookedByYear(listing, year):
    dataset = sortDataByListingIdBooked(listing)
    mask = dataset['date'].dt.year == year
    newDataset = dataset[mask]

    return newDataset

def sortMonthlyDataByListingIdByBooked(listing, year, month):
    dataset = sortDataByListingIdBookedByYear(listing, year)
    mask = dataset['date'].dt.month == month
    newDataset = dataset[mask]

    return newDataset



