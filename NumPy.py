# Ejay Aguirre
# 10/28/2024
import numpy as np

# 1. Import numpy as np and print the version number. (5 Points)
print("numpy version:", np.__version__)

# 2. Create a 1D array of numbers from 0 to 9. Desired output (10 points)
Array = np.arange(10)
print(Array)

# 3. Import a dataset with numbers and texts keeping the text intact in python numpy.
dataURL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = np.genfromtxt(dataURL, delimiter=',', dtype=None)

print(data)

# 4. Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset.
dataURL2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data2 = np.genfromtxt(dataURL2, delimiter=',', dtype=None)

petalWidth = data2['f3'].astype(float)
index = np.argmax(petalWidth > 1.0)

print("Postion of the first occurace of a value greater than 1.0: ", index)
# 5. From the array a, replace all values greater than 30 to 30 and less than 10 to 10.

np.random.seed(100)
a = np.random.uniform(1,50, 20)

a[a > 30] = 30
a[a < 10] = 10

print(a)
