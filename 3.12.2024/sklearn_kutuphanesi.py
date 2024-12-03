#kütüphanleri yükle
from sklearn.datasets import load_iris
import numpy as np
#veri seti yükle
iris=load_iris()
data=iris.data
ortalama=np.mean(data, axis=0) #ortalama hesapla
varyans=np.var(data, axis=0) #varyans hesaplama
stdsapma=np.std(data, axis=0) #standart sapma
print(f"ortalama={ortalama}\nvaryans={varyans}\nstandart sapma={stdsapma}")

from scipy.stats import mode
#ortanca değer hesaplama
ortanca=np.median(data, axis=0)
#en sık tekrar eden değerler:
median_deger, median_sayı=mode(data, axis=0)
#Konsolda yazdırma
print(f'ortanca={ortanca}\nmedian değer={median_deger}\nmedian sayı={median_sayı}')











# from scipy.stats import mode
# #medyan ortanca değer hesaplama
# medyan=np.median(data, axis=0)
# #en sık tekrar eden değer
# median_degeri, median_sayılar=mode(data, axis=0)
# #görüntüle:
# print(F"ortanca değer:{medyan}\nmediyan değeri:{median_degeri[0]}\nmedyan sayıları:{median_sayılar[0]}")