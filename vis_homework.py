# Ejay Aguirre
# 11/25/2024

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 09:47:55 2021

@author: u6026797
"""
#%% libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%% data

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
covid_df = pd.read_csv(url, index_col=0)

#%% Instructions
'''
Overall instructions:
As described in the homework description, each graphic you make must:
   1. Have a thoughtful title
   2. Have clearly labelled axes 
   3. Be legible
   4. Not be a pie chart
I should be able to run your .py file and recreate the graphics without error.
As per usual, any helper variables or columns you create should be thoughtfully
named.
'''
# Print out the column names
# print(covid_df.columns.tolist())


#%% viz 1
'''
Create a visualization that shows all of the counties in Utah as a time series,
similar to the one shown in slide 22 during the lecture. The graphic should
-Show cases over time
-Have all counties plotted in a background color (something like grey)
-Have a single county plotted in a contrasting color (something not grey)
-Have well formatted dates as the X axis
'''
# Create dataframe for only Utah
utahData = covid_df[covid_df["Province_State"] == "Utah"]

# Collect counties from the Utah DataFrame
counties = utahData["Admin2"]
dateColumns = utahData.columns[11:]
utahCases = utahData[dateColumns].transpose()
utahCases.columns = counties
utahCases.index = pd.to_datetime(dateColumns)

highlight = "Salt Lake"

# Plot data
plt.figure(figsize=(12,6,))
for county in counties:
    plt.plot(utahCases.index, utahCases[county], color="gray")

plt.plot(utahCases.index, utahCases[highlight], color="blue", label=f"{highlight} County")

# Plot Information
plt.title("COVID-19 Cases Over time in Utah Counties")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.legend(loc="upper left")
plt.grid(True, which="major", linestyle="--")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#%% viz 2
'''
Create a visualization that shows the contrast between the county in Utah with
the most cases to date to a county in Florida with the most cases to date.
The graphic should:
-Have only two counties plotted
-Highlight the difference between the two comparison counties
You may use any style of graphic you like as long as it is effective (dense)
and readable
'''

# Create dataframe for Utah & Florida
dateColumns = covid_df.columns[11:]
utahData = covid_df[covid_df["Province_State"] == "Utah"]
floridaData = covid_df[covid_df["Province_State"] == "Florida"]

# Most cases in Utah Counties
utahMostCases = utahData.iloc[:,-1].idxmax()
utahCountyMax = utahData.loc[utahMostCases, "Admin2"]
utahMaxCases = utahData.loc[utahMostCases, dateColumns]

# Most cases in Florida Counties
floridaMostCases = floridaData.iloc[:,-1].idxmax()
floridaCountyMax = floridaData.loc[floridaMostCases, "Admin2"]
floridaMaxCases = floridaData.loc[floridaMostCases, dateColumns]

# Datetime Column
dates = pd.to_datetime(dateColumns)

# Plot Data Comparison
plt.figure(figsize=(12, 6))
plt.plot(dates, utahMaxCases, label=f"{utahCountyMax} County in Utah", color="red")
plt.plot(dates, floridaMaxCases, label=f"{floridaCountyMax} County in Utah", color="blue")

# Plot Information
plt.title("Comparison of COVID-19 Cases: Utah vs. Florida")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases (Cumlative)")
plt.legend(loc="upper left")
plt.grid(True, linestyle="--")
plt.xticks(rotation=45,)
plt.tight_layout()
plt.show()

#%% viz 3
'''
Create a visualization that shows BOTH the running total of cases for a single
county AND the daily new cases. The graphic should:
-Use two y-axes (https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
-Use color to contrast the two series being plotted
-Have well formatted dates as the X axis
'''
# Create DataFrames
dateColumns = covid_df.columns[11:]
utahData = covid_df[covid_df["Province_State"] == "Utah"]
saltLakeData = utahData[utahData["Admin2"] == "Salt Lake"]

# Filter the DataFrames
saltLakeCases = saltLakeData[dateColumns].iloc[0].astype(float)
newCases = saltLakeCases.diff().fillna(0)

# Only have the values
SaltLakeCases = saltLakeCases.values
NewCases = newCases.values

dates = pd.to_datetime(dateColumns)

# Plot the data
fig, ax1 = plt.subplots(figsize=(12,6))

ax1.plot(dates, SaltLakeCases, color="blue", label="Running Total of Cases")
ax1.set_xlabel("Date")
ax1.set_ylabel("Running Total of Cases", color="Blue")
ax1.tick_params(axis="y", labelcolor="blue")
ax1.grid(True, linestyle="--")

# Include two y-axis
ax2 = ax1.twinx()
ax2.plot(dates, NewCases, color="red", label="Daily New Cases")
ax2.set_ylabel("Daily New Cases", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# Plot Information
plt.title(f"COVID-19 Runnign Total and Daily New Cases: Salt Lake Count, Utah")
plt.xticks(rotation=45)
plt.tight_layout()

fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.show()

#%% viz 4
'''
Create a visualization that shows a stacked bar chart of county contributions
to a given state's total cases. You may choose any state (or states).
(https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
The graphic should:
-Have a single column delineate a state
-Have each 'slice' or column compontent represent a county
'''
# Set DataFrames
dateColumns = covid_df.columns[11:]
utahData = covid_df[covid_df["Province_State"] == "Utah"]

utahCounties = utahData["Admin2"]
casesByCounty = utahData.iloc[:,-1]

# Plot Data
fig, ax = plt.subplots(figsize=(10,8))
ax.bar(counties, casesByCounty, color="blue", label="Total Cases")

# Plot Information
ax.set_title(f"County Contributions to Total COVID-19 Cases in Utah")
ax.set_xlabel("Counties")
ax.set_ylabel("Total Cases")
ax.tick_params(axis="x", rotation=90)
ax.grid(axis="y", linestyle="--")
ax.legend(loc="upper right")

plt.tight_layout()
plt.show()

#%% extra credit (5 points)
'''
Use Seaborn to create a grouped box plot of all reported states. Each boxplot
should be a distinct state. Have the states ordered from most cases (FL) to fewest 
cases. (https://seaborn.pydata.org/examples/grouped_boxplot.html)
'''
# Set DataFrames
stateTotal = covid_df.groupby("Province_State").sum()
stateTotal["Total_Cases"]= stateTotal.iloc[:, 11:].sum(axis=1)
sortStates = stateTotal.sort_values("Total_Cases", ascending=False).index

# Clean Data for Ploting
formatData = covid_df.melt(
    id_vars = ["Province_State"],
    value_vars = covid_df.columns[11:],
    var_name = "Date",
    value_name = "Cases"
)
formatData = formatData.groupby(["Province_State", "Date"]).sum().reset_index()
formatData["Date"] = pd.to_datetime(formatData["Date"])
formatData["Province_State"] = pd.Categorical(formatData["Province_State"], categories=sortStates, ordered=True)

# Plot Data with Seaborn
plt.figure(figsize=(16, 10))
sns.boxplot(
    x="Province_State",
    y="Cases",
    data=formatData,
    order=sortStates,
    palette="coolwarm"
)

# Plot Information
plt.title("Grouped Boxplot of COVID-19 Cases by State (Ordered by Total Cases")
plt.xlabel("State")
plt.ylabel("Cases")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
    