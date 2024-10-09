import pandas as pd
from geopy.geocoders import OpenCage
import time

# Load the list of places from a CSV file
df = pd.read_csv('program_names.csv')  # Replace 'places.csv' with your actual CSV file path

# Initialize the OpenCage geocoder (requires a free API key)
geolocator = OpenCage(api_key='e0ae849849e540b09a3ab3af1ba9cdab')

# Create a list to store the results
address_data = []

# Iterate over each place in the DataFrame
for index, row in df.iterrows():
    place_name = row['Place']
    try:
        location = geolocator.geocode(place_name)
        if location:
            address = location.address
        else:
            address = "Address not found"
        
        # Store the result
        address_data.append({'Place': place_name, 'Address': address})

        # Print the program name and address to verify progress
        print(f"Found: {place_name} -> {address}")

    except Exception as e:
        address_data.append({'Place': place_name, 'Address': 'Error occurred'})
        print(f"Error retrieving address for {place_name}: {e}")

    # Increase sleep time to avoid being rate limited
    time.sleep(3)

# Create a DataFrame to hold the places and addresses
address_df = pd.DataFrame(address_data)

# Save the DataFrame to a new CSV file
address_df.to_csv('places_with_addresses.csv', index=False)

print("Addresses have been successfully saved to 'places_with_addresses.csv'.")
