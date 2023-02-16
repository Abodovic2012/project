import requests
import json
import pandas as pd
import time

params = {
  'access_key': 'b22f3a1b9dce71f48c233cc9f9462a22',
  'dep_iata': 'WAW','dep_iata': 'GDN','dep_iata': 'KTW','dep_iata': 'POZ','dep_iata': 'WRO',


}

api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()

# Extract the 'data' list from the 'api_response' dictionary
data = api_response['data']

# Create a Pandas DataFrame from the 'data' list
df = pd.DataFrame(data, columns=['flight_date', 'airline', 'flight', 'flight_status'])

# Set the maximum number of columns to display
pd.set_option('display.max_columns', None)

# Print the first 100 rows of the DataFrame
time.sleep(10)
print(df.head(70))
