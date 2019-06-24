import pandas as pd
import numpy as np

seattleListings = pd.read_csv(r'C:\Users\karan.shah05\PycharmProjects\AirBnB vs Rental in Seattle\Data\AirbnbData\calendar.csv', sep=',')

seattleListingsAddresses = pd.read_csv(r'C:\Users\karan.shah05\PycharmProjects\AirBnB vs Rental in Seattle\Data\AirbnbData\listings.csv', sep=',')

seattleListingsAddressesModified = seattleListingsAddresses[['id', 'host_neighbourhood', 'latitude', 'longitude', 'property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'bed_type', 'price', 'weekly_price', 'monthly_price', 'security_deposit', 'cleaning_fee', 'guests_included', 'extra_people', 'minimum_nights', 'maximum_nights', 'street']]

seattleListingsDates = seattleListings[['listing_id', 'date', 'available']]

mainData = seattleListingsDates.merge(seattleListingsAddressesModified, how='inner', left_on='listing_id', right_on='id')

export_csv = mainData.to_csv(r'C:\Users\karan.shah05\PycharmProjects\AirBnB vs Rental in Seattle\Data\AirbnbData\mainData.csv', index=None, header=True)
