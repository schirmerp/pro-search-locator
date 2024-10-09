import pandas as pd
from geopy.geocoders import Nominatim
import time

# Load the list of places from a CSV file
df = pd.read_csv('program_names.csv')  # Replace 'places.csv' with your actual CSV file path

# Initialize the Nominatim geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

# Create a list to store the results
address_data = []

# Iterate over each place in the DataFrame
for index, row in df.iterrows():
    place_name = row['Place']  # Assuming your CSV has a column named 'Place'
    try:
        location = geolocator.geocode(place_name)
        if location:
            address = location.address
        else:
            address = "Address not found"
        address_data.append({'Place': place_name, 'Address': address})
    except Exception as e:
        address_data.append({'Place': place_name, 'Address': 'Error occurred'})
        print(f"Error retrieving address for {place_name}: {e}")

    # Add a delay to prevent overwhelming the server (comply with OpenStreetMap's rate limits)
    time.sleep(1)

# Create a DataFrame to hold the places and addresses
address_df = pd.DataFrame(address_data)

# Save the DataFrame to a new CSV file
address_df.to_csv('places_with_addresses.csv', index=False)

print("Addresses have been successfully saved to 'places_with_addresses.csv'.")
