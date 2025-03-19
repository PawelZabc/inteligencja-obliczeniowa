import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import math
df = pd.read_csv("dane.csv")

# print(df)



def f_act(x):
 return 1/(1+math.e**(-x))

def forwardPass(wiek, waga, wzrost):
 hidden1 = (wiek * -0.46122) +  (waga * 0.97314) + (wzrost * -0.39203) + 0.80109
 hidden1_po_aktywacji = f_act(hidden1)
 hidden2 = wiek * 0.78548 + waga * 2.10684 + wzrost * -0.57847
 hidden2_po_aktywacji = f_act(hidden2)
 output = hidden1_po_aktywacji * -0.81546 + hidden2_po_aktywacji * 1.03775 + -0.2368
 return output




for index, row in df.iterrows():
    print(f"Index: {index}, wiek: {row['wiek']}, waga: {row['waga']}, wzrost: {row['wzrost']}")
    wynik = forwardPass(row['wiek'],row['waga'],row['wzrost'])
    print(wynik)
    if (wynik>=0.5)==row['gra']:
      print("Poprawnie")
    else:
      print("Nie poprawnie")