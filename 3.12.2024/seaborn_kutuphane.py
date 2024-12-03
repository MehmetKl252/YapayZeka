import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris
















# veri seti yükleme(iris)
iris=load_iris()
data=iris.data
#baslik=iris.baslik
#onceki_ad=iris.onceki_ad
# veri setini görselleştirme
sns.pairplot(sns.load_dataset("iris", hue="species"))
print(plt.show())