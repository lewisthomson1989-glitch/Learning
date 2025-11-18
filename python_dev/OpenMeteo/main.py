import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
import matplotlib.pyplot as plt
import time
import numpy as np

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
		"daily": ["precipitation_sum", "temperature_2m_max", "temperature_2m_min", "wind_speed_10m_max"],
	}

	responses = openmeteo.weather_api(API_URL, params=params)
	response = responses[0]

	daily = response.Daily()
	daily_precipitation_sum = daily.Variables(0).ValuesAsNumpy()
	daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
	daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()
	daily_wind_speed_10m_max = daily.Variables(3).ValuesAsNumpy()
    

	daily_data = {"date": pd.date_range(
    	start = pd.to_datetime(daily.Time(), unit="s", utc=True),
    	end =  pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
    	freq = pd.Timedelta(seconds=daily.Interval()),
    	inclusive = "left"
    ),
    	"precip_sum": daily_precipitation_sum,
    	"temp_min": daily_temperature_2m_min,
    	"temp_max": daily_temperature_2m_max,
		"wind_max": daily_wind_speed_10m_max
		
    }

	df = pd.DataFrame(data=daily_data)
	df['city'] = city["name"]
	WEATHER.append(df)

WEATHER = pd.concat(WEATHER, ignore_index=True)
#print(WEATHER)
WEATHER = WEATHER.set_index(["city", "date"])

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
WEATHER["temp_range"] = WEATHER["temp_max"] - WEATHER["temp_min"]
city_range = WEATHER.groupby(['city', 'date'])["temp_range"].first()
print(city_range)

# 1d. Calculate the daily max wind speed for each city.
city_max_wind = WEATHER.groupby(['city', 'date'])["wind_max"].max()
print(city_max_wind)




# Checking average calc from above is correct.
#average_max = WEATHER.loc['Sydney', 'temp_max']
#for a in average_max:
#	average = average_max.mean()
#print(average)


#precip_column = WEATHER.loc['Tokyo', 'precip_sum']
#for n in precip_column:
#    average_precip = precip_column.mean()
#print(precip_column)
#print(average_precip)
#first_col = df.iloc[:, 1] 
#print(first_col)

###############################################################################

#print(WEATHER)
print(WEATHER.columns) # 'precip_sum', 'temp_min', 'temp_max', 'wind_max', 'temp_avg', 'temp_range'
print(WEATHER.index)   # 'city', 'date' (MultiIndex)


cities = WEATHER.index.levels[0]
dates = WEATHER.index.levels[-1]
dates = sorted(dates)

x = np.arange(len(dates))

num_cities = len(cities)
num_dates = len(dates)
group_gap = 0.2

bar_width = (1 -  group_gap) / num_cities
print(bar_width)
multiplier = 0

plt.figure(figsize=(12, 6))

for city_index, city in enumerate(cities):  
    group_data = WEATHER.xs(city, level="city").reindex(dates)
    print(group_data)
    
    #group_data = group_data.reindex(dates)
    offset = (city_index - (num_cities - 1) / 2) * bar_width
    avg_temp = (group_data['temp_max'] + group_data['temp_min']) / 2
    plt.bar(x + offset,
            group_data['temp_max'] - group_data['temp_min'],
            bottom=group_data['temp_min'], 
            width=bar_width, 
            alpha=0.5, 
            edgecolor='black', 
            label=city
            )
    
    plt.plot(x + offset, avg_temp, marker='o', linestyle='-', label=f"{city} Avg")
    #multiplier += 1


plt.xticks(x, dates)
plt.xticks(rotation=90)
#plt.tight_layout()
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('City Temperatures')
plt.legend()
plt.show()


ax = plt.axes(projection='3d')

x_pos = np.arange(num_dates)
y_pos = np.arange(num_cities)



for city_index, city in enumerate(cities):  
    group_data = WEATHER.xs(city, level="city").reindex(dates)

    z_values = group_data['temp_max'].values
    #print(z_values)
    ys = np.full(num_dates, city_index)
    #print(ys)
    z_base = np.zeros(num_dates)
    #print(z_base)

    x_dimension = 0.4
    y_dimension = 0.4
    dz = z_values

    ax.bar3d(x_pos, ys, z_base, x_dimension, y_dimension, dz, alpha=0.5)

ytick_pos = y_pos +y_dimension / 2

plt.xticks(x, dates, rotation=45)
plt.yticks(ytick_pos, cities, rotation=45)
plt.xlabel('dates')
plt.ylabel('city')
plt.show()




#plt.bar(WEATHER["city"], WEATHER["temp_max"], width=bar_width, color="orange", edgecolor="black")
#plt.bar(WEATHER["city"], WEATHER["temp_min"], width=bar_width, color="green", edgecolor="black")
#plt.plot(WEATHER["date"], WEATHER["temp_avg"], marker='o', color="purple")
# TODO: 2 - Visualisation.
#	2a. Line plot - Temperature trends over 7 days for all cities.
#plt.bar(WEATHER["date"], WEATHER["temp_max"]-WEATHER["temp_min"], width=0.25, bottom=WEATHER["temp_min"], color='lightblue', edgecolor='black')

#plt.bar(WEATHER["city"], WEATHER["temp_max"], color='red')
#plt.bar(WEATHER["city"], WEATHER["temp_min"], color='blue')
#plt.xlabel("Cities")
#plt.ylabel("Temperature (°C)")
#plt.title("Cities average temps")
#
#plt.show()
##time.sleep(10)
#plt.close()

#	2b. Bar chart - Average temperature by city.

#plt.bar(WEATHER[:7]["temp_max"], color='red')
#plt.bar(WEATHER[:7]["temp_min"], color='blue')
#plt.bar(WEATHER["temp_max"], height=0.2)
#plt.show()
#	2c. Line plot - Temperature range (min-max) per city, per day.

###############################################################################
