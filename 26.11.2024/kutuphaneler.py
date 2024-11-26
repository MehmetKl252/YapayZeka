import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
veri=pd.read_csv(r"C:\Users\muhasebe\.anaconda\proje\iris.csv")
# print(veri.head())
# print(veri.columns) # sütun başlıkları görüntüleme
# print(veri.info()) # sütun veri tipi bilgilerini görüntüleme
print(veri.describe())