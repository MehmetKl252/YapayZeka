import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
# Iris veri setini yükleme
iris = load_iris()
data = iris.data
target = iris.target
feature_names = iris.feature_names

# Veri setini görselleştirme ///////////////////////////////
sns.pairplot(sns.load_dataset("iris"), hue="species")
# print(plt.show())

# Veri Setini Eğitim ve Test Verilerine Ayırma: ///////////////////////////////
from sklearn.model_selection import train_test_split

# Veri setini eğitim ve test verilerine ayırma
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

# Sınıflandırma Modeli Eğitme (Örnek olarak K-Nearest Neighbors): ///////////////////////////////
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# K-Nearest Neighbors (KNN) sınıflandırma modeli ///////////////////////////////
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Modeli kullanarak tahmin yapma ///////////////////////////////
y_pred = knn.predict(X_test)

# Doğruluk skoru hesaplama ///////////////////////////////
accuracy = accuracy_score(y_test, y_pred)
# print("Model Doğruluğu:", accuracy)

import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset("iris")
# Veri setini görselleştirme
sns.pairplot(sns.load_dataset("iris"), hue="species")
plt.show()
# print(iris)