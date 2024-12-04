import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Iris veri setini yükleme
iris = load_iris()
data = iris.data
target = iris.target
# Daha sonra, K-Means kümeleme algoritmasını kullanarak verileri kümelere ayıralım:

# K-Means modeli oluşturma
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(data)

# Küme merkezlerini ve kümeleri görselleştirme
plt.scatter(data[:, 0], data[:, 1], c=clusters, cmap='viridis')
plt.scatter(data[:, 2], data[:, 3], c=clusters, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], marker='x', c='red', s=200)
plt.scatter(centers[:, 2], centers[:, 3], marker='x', c='red', s=200)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('K-Means Clustering of Iris Dataset')
plt.show()