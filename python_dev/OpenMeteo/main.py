import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

# Tools: requests, pandas, numpy, matplotlib, seaborn (a virtual environment)

cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

CITIES = [
	{"name": "London", "latitude": 51.5074, "longitude": -0.1278},
	{"name": "Paris", "latitude": 48.8566, "longitude": 2.3522},
	{"name": "New York", "latitude": 40.7128, "longitude": -74.0060},
	{"name": "Tokyo", "latitude": 35.6762, "longitude": 139.6503},
	{"name": "Sydney", "latitude": -33.8688, "longitude": 151.2093}
]

WEATHER = []

API_URL = 'https://api.open-meteo.com/v1/forecast'
    
###############################################################################

# TODO: 0 - Fetch data. Format into dataframe.

for city in CITIES:
	params = {
		"latitude": city["latitude"],
		"longitude": city["longitude"],
		"daily": ["precipitation_sum", "temperature_2m_min", "temperature_2m_max"],
	}

	responses = openmeteo.weather_api(API_URL, params=params)
	response = responses[0]

	daily = response.Daily()
	daily_precipitation_sum = daily.Variables(0).ValuesAsNumpy()
	daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
	daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()

	daily_data = {"date": pd.date_range(
    	start = pd.to_datetime(daily.Time(), unit="s", utc=True),
    	end =  pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
    	freq = pd.Timedelta(seconds=daily.Interval()),
    	inclusive = "left"
    ),
    	"precip_sum": daily_precipitation_sum,
    	"temp_min": daily_temperature_2m_min,
    	"temp_max": daily_temperature_2m_max
    }

	df = pd.DataFrame(data=daily_data)
	df['city'] = city["name"]
	WEATHER.append(df)

WEATHER = pd.concat(WEATHER, ignore_index=True)
WEATHER = WEATHER.set_index(["city", "date"])
print(WEATHER)
###############################################################################

# TODO: 1 - Analysis.
#	1a. Find city with highest/lowest average temperature.
#	1b. Identify warmest/coldest day per city.
#	1c. Calculate temperature ranges (min-max) per city, per day.
precip_column = df['precip_sum']
print(precip_column)

###############################################################################

# TODO: 2 - Visualisation.
#	2a. Line plot - Temperature trends over 7 days for all cities.
#	2b. Bar chart - Average temperature by city.
#	2c. Line plot - Temperature range (min-max) per city, per day.

###############################################################################
