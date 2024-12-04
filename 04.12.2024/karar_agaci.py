from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Iris veri setini yükleme //////////////////////////////
iris = load_iris()
X = iris.data  # Özellikler
y = iris.target  # Etiketler
# Veri setini eğitim ve test setlerine bölelim: //////////////////////////////
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Karar ağacı modelini oluşturalım ve eğitelim: //////////////////////////////
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
# Modeli kullanarak tahminler yapalım ve doğruluk (accuracy) değerini değerlendirelim: //////////////////////////////
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
# print("Doğruluk (Accuracy):", accuracy) # Doğruluk (Accuracy): 1.0

from sklearn import tree
import matplotlib.pyplot as plt
# Iris veri setini yükleme //////////////////////////////
# iris = load_iris()
# X = iris.data  # Özellikler
# y = iris.target  # Etiketler
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)
plt.figure(figsize=(20,10))
tree.plot_tree(model,
               feature_names=iris["feature_names"],
               rounded=True,
               filled=True, #renklendirme renk ile doldurma
               impurity=True)
print(plt.show())