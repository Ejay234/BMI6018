# Ejay Aguirre
# 12.02.2024

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from ucimlrepo import fetch_ucirepo

# Fetch the dataset
data = fetch_ucirepo(id=296)

# Dataframe
df = data.data.features

# Data Cleaning
df_numeric = df.select_dtypes(include=[np.number])
scaler = StandardScaler()
dfScaled = scaler.fit_transform(df_numeric)

# Calculate Sum of Squared Errors (SSE) for different values of k
sse = []
k_values = range(1, 11)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(dfScaled)
    sse.append(kmeans.inertia_)

# Plot the SSE vs. k to find the elbow
plt.figure(figsize=(8, 5))
plt.plot(k_values, sse, marker='o')
plt.title("Elbow Method for Optimal k")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Sum of Squared Errors (SSE)")
plt.xticks(k_values)
plt.grid()
#plt.savefig("elbow_plot.png", dpi=300, bbox_inches='tight')
plt.show()

# The elbow plot shows a significant  drop in SEE from 1 to 3
# After 3, the decrease slows down, which indicates diminishing returns for adding more clusters
# Hence, k=3 is chosen as the optimal number

# Set the optimal number
optimal_k = 3

# Perform K-means clustering with the optimal k
kmeansOptimal = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeansOptimal.fit_predict(dfScaled)

# Add cluster labels to the dataset for visualization
df['Cluster'] = clusters

# Plot the clusters and their centroids
plt.figure(figsize=(8, 5))
for cluster in range(optimal_k):
    clusterData = dfScaled[clusters == cluster]
    plt.scatter(clusterData[:, 0], clusterData[:, 1], label=f'Cluster {cluster + 1}')

centroids = kmeansOptimal.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], color='red', marker='X', s=200, label='Centroids')

plt.title("Clusters with Centroids")
plt.xlabel("Feature 1 (scaled)")
plt.ylabel("Feature 2 (scaled)")
plt.legend()
plt.grid()
# plt.savefig("clusters_with_centroids.png", dpi=300, bbox_inches='tight')
plt.show()

# The scatter plot shows three distinct clusters with their centroids marked with an "X"
# Each cluster represents a group of data points that are closer to their respective centeroids
# This clustering aligns with the elbow method's suggestion of k = 3