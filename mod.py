import requests
import json
import pandas as pd
import time

# List of all airports in Poland
airports = ['WAW', 'KRK', 'GDN', 'KTW', 'POZ', 'WRO', 'LUZ', 'SZY', 'RZE', 'BZG', 'LCJ', 'SZZ', 'BIA', 'OSR', 'IEG', 'RDO', 'RNB', 'SZZ', 'Szwederowo', 'WMI']

# Create an empty list to store the flight data
flight_data = []

# Loop through all airport combinations for departure and arrival
for dep_airport in airports:
    for arr_airport in airports:
        # Skip if the departure and arrival airport are the same
        if dep_airport == arr_airport:
            continue
        
        # Define the API request parameters
        params = {
            'access_key': '9bb0de481968d410bdc93ec10f39b560',
            'dep_iata': dep_airport,
            'arr_iata': arr_airport
        }

        # Make the API request
        api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
        
        # Wait for 10 seconds to avoid API rate limiting
        
        # Parse the API response and append the flight data to the list
        api_response = api_result.json()
        
        if 'data' in api_response:
            flight_data.extend(api_response['data'])
        else:
            print(f"API response does not contain flight data for {dep_airport} to {arr_airport}: {api_response}")
        
# Create a Pandas DataFrame from the flight data
df = pd.DataFrame(flight_data, columns=['flight_date', 'airline', 'flight', 'flight_status', 'departure', 'arrival'])

# Set the maximum number of columns to display
pd.set_option('display.max_columns', None)

# Print the first 100 rows of the DataFrame
print(df.head(100))
