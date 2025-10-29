import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after= 3600)
retry_session = retry(cache_session, retries= 5, backoff_factor= 0.2)
openmeteo = openmeteo_requests.Client(session= retry_session)


CITIES = {
	'London': (51.5074, -0.1278),
	'Paris': (48.8566, 2.3522),
	'New York': (40.7128, -74.0060),
	'Tokyo': (35.6762, 139.6503),
	'Sydney': (-33.8688, 151.2093)
}

API_URL = 'https://api.open-meteo.com/v1/forecast'
# Params:	latitude, longitude, 
#			daily=temperature_2m_max,temperature_2m_min,
#			precipitation_sum, timezone=auto
params = {"latitude": CITIES['London'][0],
          "longitude": CITIES['London'][1],
          "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
          "timezone": "auto",
          }
print(params)
# for loop needed to be used for each city.
for city in CITIES.keys():
    print(city)
responses = openmeteo.weather_api(API_URL, params=params)

response = responses[0]
print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation: {response.Elevation()} m asl")
print(f"Timezone: {response.Timezone()}{response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

daily = response.Daily()
daily_precipitation_sum = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end =  pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}

daily_data["precipitation_sum"] = daily_precipitation_sum
daily_data["temperature_2m_max"] = daily_temperature_2m_max
daily_data["temperature_2m_min"] = daily_temperature_2m_min

daily_dataframe = pd.DataFrame(data = daily_data)
print("\nDaily data\n", daily_dataframe)
# Tools: requests, pandas, numpy, matplotlib, seaborn (a virtual environment)

###############################################################################

# TODO: 0 - Fetch data. Comes as json. Format into dataframe.


# TODO: 1 - Analysis.
#	1a. Find city with highest/lowest average temperature.
#	1b. Identify warmest/coldest day per city.
#	1c. Calculate temperature ranges (min-max) per city, per day.

# TODO: 2 - Visualisation.
#	2a. Line plot - Temperature trends over 7 days for all cities.
#	2b. Bar chart - Average temperature by city.
#	2c. Line plot - Temperature range (min-max) per city, per day.

###############################################################################

