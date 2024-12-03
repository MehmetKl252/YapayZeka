import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

veri={
    "Alan-m2":[50,60,80,90,100,120],
    "Oda-sayısı":[1,2,2,3,3,4],
    "Yaş":[5,10,20,15,10,5],
    "MerkezUzaklık-km":[2,3,5,8,6,1],
    "Fiyatı-TL":[850000,2000000,2400000,2800000,3500000,5000000]
}
df=pd.DataFrame(veri)
# print(df)
# print(df.head())
#özellikler ve etiketler
X=df[["Alan-m2","Oda-sayısı","Yaş","MerkezUzaklık-km"]] #özellikler
y=df["Fiyatı-TL"] # etiket

#4. Veri Setini Eğitim ve Test Olarak Bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Makine Öğrenimi Modeli Eğitimi
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Test Verisi ile Tahmin
y_pred = model.predict(X_test)

# 7. Model Performansı
mse = mean_squared_error(y_test, y_pred)
print(f'\nOrtalama hata karaesi:{mse:.2f}')
# Yeni ev tahmini
yeni_ev = np.array([[90, 2, 5, 1]])  # 90 m², 3 oda, 7 yaşında, merkeze 4 km
tahmin_fiyat = model.predict(yeni_ev)
print(f'\nYeni evin tahmini fiyatı:{tahmin_fiyat[0]:,.2f} TL')











# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error

# # 1. Örnek Veri Seti
# data = {
#     "Alan (m²)": [50, 60, 70, 80, 100, 120],
#     "Oda Sayısı": [1, 2, 2, 3, 3, 4],
#     "Yaş": [5, 10, 15, 20, 10, 5],
#     "Merkez Uzaklık (km)": [2, 3, 5, 8, 6, 1],
#     "Fiyat (TL)": [200000, 250000, 300000, 400000, 350000, 500000]
# }

# # Pandas DataFrame oluştur
# df = pd.DataFrame(data)

# # 2. Veri Analizi
# print("\n### Veri Setinin İlk Satırları ###")
# print(df.head())

# print("\n### Temel İstatistikler ###")
# print(df.describe())

# # 3. Özellikler ve Etiketler (X ve y)
# X = df[["Alan (m²)", "Oda Sayısı", "Yaş", "Merkez Uzaklık (km)"]]  # Özellikler
# y = df["Fiyat (TL)"]  # Etiket

# # 4. Veri Setini Eğitim ve Test Olarak Bölme
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # 5. Makine Öğrenimi Modeli Eğitimi
# model = LinearRegression()
# model.fit(X_train, y_train)

# # 6. Test Verisi ile Tahmin
# y_pred = model.predict(X_test)

# # 7. Model Performansı
# mse = mean_squared_error(y_test, y_pred)
# print(f"\n### Ortalama Hata Karesi (MSE): {mse:.2f} ###")

# # 8. Örnek Tahmin
# yeni_ev = np.array([[90, 3, 7, 4]])  # 90 m², 3 oda, 7 yaşında, merkeze 4 km
# tahmin_fiyat = model.predict(yeni_ev)
# print(f"\n### Yeni Evin Tahmini Fiyatı: {tahmin_fiyat[0]:,.2f} TL ###")





