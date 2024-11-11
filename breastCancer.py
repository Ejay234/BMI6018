from ucimlrepo import fetch_ucirepo 
import pandas as pd
import numpy as np

# Ejay Aguirre
# 11.11.2024

# fetch dataset 
breastCancer = fetch_ucirepo(id=14) 

# data (as pandas dataframes) 
x = pd.DataFrame(breastCancer.data.features)
print(x.head()) # prints out the features (varibles) with the following data from the dataset breast_cancer

# creating an id index for later use (starting at instance 1). Will be use for the following functions.
x['id'] = np.arange(1, len(x) + 1)

# write code to demonstrate the following Pandas functions:
# Melt
# The following function will melt the dataframe to rows, no particular id_variable will be assigned
meltFrame = x.melt(id_vars='id', var_name='Feature', value_name='Value')
print("Melt Function:\n", meltFrame)

# Pivot
# The pivot function returns the melt data frame into a cleaner frame with the inclusion of id
pivotFrame = meltFrame.pivot(index='id', columns='Feature', values='Value')
print("Pivot Function:\n", pivotFrame)

# Aggregation
# The agg function will insert statisical functions regarding the sum, max, and min, of the variable, deg-malig 
aggFrame = pivotFrame['deg-malig'].agg(['sum', 'min', 'max'])
print("Agg Function:\n", aggFrame)

# Iteration
# This function is to verify the results from the aggFrame feature, deg-malig
degMaligSum = 0;
degMaligMax = 0;
degMaligMin = 1000;
for key, value in pivotFrame.items():
    if key == 'deg-malig':
        for val in value:
            degMaligSum += val
            if val > degMaligMax:
                degMaligMax = val
            if val < degMaligMin:
                degMaligMin = val
print("Items Function:")
print("Sum:", degMaligSum)
print("Max:", degMaligMax) 
print("Min:", degMaligMin)

# Groupby
# The following function will make a frame of deg-malig, incorportated agg functions that will be groupby age.
if 'age' in x.columns:
    groupFrame = x.groupby('age').agg({
        'deg-malig': ['sum', 'min', 'max'],
    })
    print("GroupBy Function:\n", groupFrame)


