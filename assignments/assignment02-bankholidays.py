# This program prints out the bank holiddays that happen in Northen Ireland
# Author: Hewa Orang

# reference: 
    # https://docs.python.org/3/library/stdtypes.html#str.startswith
    # https://docs.python.org/3/reference/lexical_analysis.html#f-strings

# Import the requests library to handle HTTP requests
import requests

url =" https://www.gov.uk/bank-holidays.json"              # URL for UK bank holidays API
response = requests.get(url)                               # Send a GET request to the API
data = response.json()                                     # Parse the JSON response into a Python dictionary  
# print (data)

other_uk_dates = set()  # Create an empty set to store other UK holidays

for event in data['england-and-wales']['events']:          # Loop through England and Wales events
    if event['date'].startswith('2025'):                   # Check if the event date starts with '2025'  
        other_uk_dates.add((event['title'], event['date']))     # Add the event title and date as a tuple to the set

for event in data['scotland']['events']:
    if event['date'].startswith('2025'):
        other_uk_dates.add((event['title'], event['date']))

# Print Northern Ireland holidays.
for event in data['northern-ireland']['events']:
    if event['date'].startswith('2025'):
        print(f"{event['title']} on {event['date']}")

# Print Northern Ireland holidays that are not in other UK holidays

for event in data['northern-ireland']['events']:
    if event['date'].startswith('2025'):
        ni_holiday = (event['title'], event['date']) # Create a tuple for the Northern Ireland holiday
        if ni_holiday not in other_uk_dates:
            print(f"Holidays unique to Northern Ireland:")
            print(f" {event['title']} on {event['date']}")
