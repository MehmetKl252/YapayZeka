import pandas as pd
import numpy as np
isimler=pd.Series(["berkay","ziyad","neslihan"])
# print(isimler)
#pandas ile sözlük kullanımı
veriler={
    "ad":["ali","veli","handan"],
    "soyad":["duran","çalışkan","ışık"],
    "adres":["esenyurt","avcılar","beylikdüzü"],
    "yaş":[25,30,28]
}
df=pd.DataFrame(veriler)
# print("Tablo bilgileri:")
# print(df)
# Yaşı 25'ten büyük olan kişileri listeleyiniz
#adrese göre df listeleme
adres=df[df["adres"]=="esenyurt"]
# print(adres)
#yaş ortalamasını bulma:
ortalama=df["yaş"].mean()
# print(ortalama)
#yeni yaş sütununda +5 yaş ekleme:
df["yaş+5"]=df["yaş"]+5
# print(df)
#verileri yaşa göre sıralama
yas_sıralama = df.sort_values(by="yaş", ascending=True)
print(yas_sıralama)