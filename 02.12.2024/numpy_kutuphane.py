import numpy as np
import pandas as pd
import cv2 as cv
# print("version",cv.__version__)

# veri seti girişi
veri={
    "Yaş":[20,25,np.nan,40,45],
    "Gelir":[25000,30000,35000,np.nan,45000],
    "Cinsiyet":["Bay","Bayan","Bayan","Bay",np.nan]
}
df=pd.DataFrame(veri)
# print(df)
#Eksik değerleri doldurma
df["Yaş"].fillna(df["Yaş"].mean(), inplace=True)
df["Gelir"].fillna(df["Gelir"].median(), inplace=True)
df["Cinsiyet"].fillna("Bilinmiyor", inplace=True)
# Kategorik verileri dönüştürme 
df_donusturme = pd.get_dummies(df, columns=["Cinsiyet"])
print(df_donusturme)