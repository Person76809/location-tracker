import requests

# Send a request to ipinfo.io to get geolocation information based on IP address
response = requests.get('https://ipinfo.io/json')
data = response.json()

# Extract the location information
city = data['city']
region = data['region']
country = data['country']
postal = data['postal']
latitude, longitude = data['loc'].split(',')

# Print the location information
print(f'City: {city}')
print(f'Region: {region}')
print(f'Country: {country}')
print(f'Postal Code: {postal}')
print(f'Latitude: {latitude}')
print(f'Longitude: {longitude}')
