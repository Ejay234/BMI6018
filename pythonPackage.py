# Ejay Aguirre
# 11/18/2024

# Introduction to Seaborn 
# Seaborn is a Python data visualization library based on Matplotlib. It provides an interface for illustrating attractive and informative statistical graphics. 
# Furthermore, Seaborn closey integrates the data structue and designed of DataFrames from Pandas, making visualization seamless.
# Overall, Seaborn simplifies the process of creating complex visualizations and makes it easier to explore and understand data. 
# https://seaborn.pydata.org/tutorial/introduction.html
 
# Advantages of Seaborn: 
# 1. Seaborn offers a high-level interface for creating informative statistical graphics.
# 2. Seaborn works well with Pandas Dataframes, which makes it easy to directly visualize data from DataFrames.
# 3. Seaborn comes with several themes and color palettes to enhance the plot's aesthetic making it easier to read and fit a theme.
# 4. Seaborn includes functions for creating a variety of types of statistical plots.
# 5. Seaborn allows the user to easily customize their plots by including elements such as labels and color
 
# Limitations of Seaborn: 
# 1. Seaborn is dependent on Matplotlib which inherients performance issues with very large datasets.
# 2. Seaborn plots are static by default and does not offer a great level of interactivitness as some other visualization libraries.
# 3. Seaborn is not typically the standard use for visualization as MatplotLib which requires a learning curve.
 
# Example code to demonstrate calling the Seaborn library and using an example dataset: 

# pip install seaborn, matplotlib, ucimlrepo
import seaborn as sns
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo 

# fetch dataset 
diabetes_130_us_hospitals_for_years_1999_2008 = fetch_ucirepo(id=296) 


# data (as pandas dataframes) 
data = diabetes_130_us_hospitals_for_years_1999_2008.data.features 

# Create a plot using Seaborn
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10,6))


sns.countplot(data=data, x="age", palette="viridis")


plt.title("Distribution of Age Groups in the Dataset")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()
# See figure 1, https://github.com/Ejay234/BMI6018/blob/main/seabornFigure1.png

# Create a plot using Seaborn
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

sns.boxplot(data=data, x='age', y='time_in_hospital', palette='muted')

# See figure 2
plt.title('Box Plot of Time in Hospital by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Time in Hospital (days)')
plt.xticks(rotation=45)
plt.show()
