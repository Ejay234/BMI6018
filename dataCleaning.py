# Ejay Aguirre
# 11/4/2024

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

flights_data = pd.read_csv('data/flights.csv')
flights_data.head(10)
weather_data_pd = pd.read_csv('data/weather.csv')
weather_data_np = weather_data_pd.to_numpy()


#Question 1 How many flights were there from JFK to SLC? Int
q_1 = flights_data[(flights_data['origin'] == 'JFK' ) & (flights_data['dest'] == 'SLC')].shape[0]
print("Question 1:")
print(q_1)

#Question 2 How many airlines fly to SLC? Should be int
q_2 = flights_data[flights_data['dest'] == 'SLC']['carrier'].nunique()
print("Question 2:")
print(q_2)

#Question 3 What is the average arrival delay for flights to RDU? float
q_3 = flights_data[flights_data['dest'] == 'RDU']['arr_delay'].mean()
print("Question 3:")
print(q_3)

#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
sea_flights = flights_data[flights_data['dest'] == 'SEA']
sea_nyc = sea_flights[(sea_flights['origin'] == 'JFK') | (sea_flights['origin'] == 'LGA')].shape[0]
q_4 = sea_nyc / sea_flights.shape[0]
print("Question 4:")
print(q_4)

#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
flights_data['date'] = pd.to_datetime(flights_data[['year', 'month', 'day']])
q_5 = flights_data.groupby('date')['dep_delay'].mean().idxmax(), flights_data.groupby('date')['dep_delay'].mean().max()
print("Question 5:")
print(q_5)

#Question 6 Which date has the largest average arrival delay? pd slice with date and float
q_6 = flights_data.groupby('date')['arr_delay'].mean().idxmax(), flights_data.groupby('date')['arr_delay'].mean().max()
print("Question 6:")
print(q_6)

#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
flights_data['speed'] = flights_data['distance'] / flights_data['air_time']
fastest_flight_index = flights_data[(flights_data['origin'].isin(['LGA', 'JFK']))]['speed'].idxmax()
fastest_flight = flights_data.loc[fastest_flight_index, ['origin', 'dest', 'speed']]
q_7 = fastest_flight
print("Question 7:")
print(q_7)

#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
q_8 = weather_data_pd.fillna(0)

#%% Numpy Data Filtering/Sorting Question Answering
#Use weather_data_np
#Question 9 How many observations were made in Feburary? Int
print(weather_data_pd.head())
monthIndex = weather_data_pd.columns.get_loc("month")
humidIndex = weather_data_pd.columns.get_loc("humid")

q_9 = np.sum(weather_data_np[:, monthIndex] == 2)
print("Question 9:")
print(q_9)

#Question 10 What was the mean for humidity in February? Float
february_humidity = weather_data_np[weather_data_np[:, monthIndex] == 2, humidIndex]
q_10 = np.mean(february_humidity)
print("Question 10:")
print(q_10)

#Question 11 What was the std for humidity in February? Float
q_11 = np.std(february_humidity)
print("Question 11:")
print(q_11)

