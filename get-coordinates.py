import requests
import time
import json
import re

def load_data_from_js_file(js_file_path):
    with open(js_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove JavaScript comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

    # Remove 'export default' and any other JS code before the array
    content = content.replace('export default', '').strip()

    # The content should now start with '[' and end with ']'
    # If it doesn't, find the start and end of the array
    array_start = content.find('[')
    array_end = content.rfind(']') + 1
    json_string = content[array_start:array_end]

    try:
        data = json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")
        return []

    return data

def geocode_address(entry):
    # Construct the address string from available components
    address_parts = [
        entry.get('address', ''),
        entry.get('city', ''),
        entry.get('state', ''),
        entry.get('zip_code', ''),
        entry.get('country', '')
    ]
    address = ', '.join(part for part in address_parts if part)
    if not address:
        print(f"No address available for {entry['name']}")
        return

    # Use Nominatim API for geocoding
    base_url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': address,
        'format': 'json',
        'limit': 1,
    }

    try:
        response = requests.get(base_url, params=params, headers={'User-Agent': 'YourAppName/1.0 (your_email@example.com)'})
        response.raise_for_status()
        results = response.json()
        if results:
            entry['lat'] = results[0]['lat']
            entry['lng'] = results[0]['lon']
            print(f"Geocoded {entry['name']}: ({entry['lat']}, {entry['lng']})")
        else:
            print(f"No results found for address: {address}")
    except requests.exceptions.RequestException as e:
        print(f"Error geocoding address {address}: {e}")
    # Respect Nominatim's usage policy by adding a delay
    time.sleep(1)

def main():
    js_file_path = 'pro-search-programs-list.js'
    data = load_data_from_js_file(js_file_path)

    if not data:
        print("No data to process.")
        return

    # Geocode all entries
    for entry in data:
        geocode_address(entry)

    # Optionally, save the updated data back to a file
    with open('pro-search-programs-list-with-coordinates.js', 'w', encoding='utf-8') as file:
        file.write('export default ')
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    main()
