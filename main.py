import pandas as pd
import numpy as np

xlsx=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(xlsx,header=0)
print(df)
#Zadanie 1
print(df[df['Liczba']>1000])
#zadanie 2
#df_imie=df[df.Imie['Imie']=='Piotr'] noidea
#print(df_imie)
#Zadanie3
suma=df["Liczba"].sum()
print(suma)
#Zadanie 4
df_2000_2005=df.loc[(df["Rok"]>=2000)&(df["Rok"]<=2005)]
sumae=df_2000_2005["Liczba"].sum()
print(sumae)

#zadanie 5
sumachlopow=df.groupby(['Plec'])
sumachlopow3=sumachlopow["Liczba"].sum()
print(sumachlopow3)

#Zadanie6
df_baby=df.loc[df["Plec"]=="K"]
df_chlopy=df.loc[df["Plec"]=="M"]
imiebab=df_baby.groupby("Rok")["Liczba"].idxmax().apply(lambda x: df.iloc[x]["Imie"])
imiechlop=df_chlopy.groupby("Rok")["Liczba"].idxmax().apply(lambda x: df.iloc[x]["Imie"])

print(imiebab)
print(imiechlop)

#Zadanie7
df_grouped=df.groupby(['Plec','Imie']).sum()
baby=df_grouped.loc['K']['Liczba'].idxmax()
krejzi=df_grouped.loc['M']['Liczba'].idxmax()
print(baby)
print(krejzi)




