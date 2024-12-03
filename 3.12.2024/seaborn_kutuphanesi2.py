import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Iris veri setini yükleme
iris = load_iris()
data = iris.data
target = iris.target
feature_names = iris.feature_names

# Veri setini görselleştirme
sns.pairplot(sns.load_dataset("iris"), hue="species")
plt.show()
