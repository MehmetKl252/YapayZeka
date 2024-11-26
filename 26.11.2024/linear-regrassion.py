import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
veri=pd.read_csv(r"C:\Users\muhasebe\.anaconda\proje\weight-height.csv")
# print(veri.head)
# print(veri.info())
x=veri["Height"]
y=veri["Weight"]
plt.scatter(x,y,c="blue")
print(plt.show())
