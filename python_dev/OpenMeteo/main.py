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
		"daily": ["precipitation_sum", "temperature_2m_max", "temperature_2m_min"],
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
    	"temp_max": daily_temperature_2m_max,
		
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

WEATHER["temp_avg"] = (WEATHER["temp_min"] + WEATHER["temp_max"]) / 2
city_avg_temps = WEATHER.groupby("city")["temp_avg"].mean()
print(city_avg_temps)  # pd.Series, not pd.DataFrame
avg_temps = {
        "highest": {"name": city_avg_temps.idxmax(), "temp": city_avg_temps.max()},
        "lowest": {"name": city_avg_temps.idxmin(), "temp": city_avg_temps.min()}
}
print(avg_temps)
#	1b. Identify warmest/coldest day per city.
city_high = WEATHER.groupby(['city', 'date'])["temp_max"].max()
city_low = WEATHER.groupby(['city', 'date'])["temp_min"].min()
abs_temps = {
    "highest": {"name": city_high.idxmax(), "temp": city_high.max()},
    "lowest": {"name": city_low.idxmin(), "temp": city_low.min()}
}
print(abs_temps)
#	1c. Calculate temperature ranges (min-max) per city, per day.


# Checking average calc from above is correct.
average_max = WEATHER.loc['Sydney', 'temp_max']
for a in average_max:
	average = average_max.mean()
print(average)


#precip_column = WEATHER.loc['Tokyo', 'precip_sum']
#for n in precip_column:
#    average_precip = precip_column.mean()
#print(precip_column)
#print(average_precip)
#first_col = df.iloc[:, 1] 
#print(first_col)

###############################################################################

# TODO: 2 - Visualisation.
#	2a. Line plot - Temperature trends over 7 days for all cities.
#	2b. Bar chart - Average temperature by city.
#	2c. Line plot - Temperature range (min-max) per city, per day.

###############################################################################
