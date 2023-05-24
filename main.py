import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image

#4 zadania
# same csv (brak excela)
# zapisywanie do pliku
#na kolosie nie ma losowych danych
#wykresy oraz kod wyslane msteams
#wykresy jako obrazy wyslane msteams
#Zadanie 1
#matplotlib jakas funkcja wykres liniowy (jakas funkcja w zadaniu i na wykresie mabyc
#zad 2
#siatka wykresy lewo prawo gora dol
#zad 3
#ramka danych grupa wykres zrobienie wykresu
#zad 4 wykres z matplotliba lub z seaborna

#Random Chart with Moving Average
# ts=pd.Series(np.random.randn(1000))
# ts=ts.cumsum()
#
# df=pd.DataFrame(ts,columns=['wartosci'])
# print(df)
# df['Srednia kroczaca']=df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()
#Histogram z siatka z kolorkiem z przezroczystoscia 0.5 superanckohaj
# x=np.random.randn(10000)
# plt.hist(x,bins=50,facecolor='y',alpha=0.5,density=True)
# plt.xlabel('Wartości')
# plt.ylabel('Prawdopodobieństwo')
# plt.title('Histogram')
# plt.grid()
# plt.show()
#Wykres kolowy matplotlib
# df=pd.read_csv('dane.csv',header=0,sep=";",decimal=".")
# print(df)
# seria=df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
# wedges, texts, autotext =plt.pie(x=seria,labels=seria.index,
#                                  autopct=lambda pct: "{:.1f}%".format(pct),
#                                  textprops=dict(color="magenta"),
#                                  colors=['blue','cyan'])
# plt.title('Suma zamówień dla sprzedawcow')
# plt.legend(loc='lower right')
# plt.ylabel('Procentowy wynik wartości zamówienia')
# plt.show()
#Wykres seaborn!
# sns.set(rc={'figure.figsize': (5, 5)})
# sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 9, 16],label='linia nr1', color='red', marker='o', linestyle=':')
# sns.lineplot(x=[1, 2, 3, 4], y=[2, 5, 10, 17],label='linia nr2', color='green', marker='^', linestyle=':')
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.title('Wykres liniowy')
# plt.show()
#Wykres seaborn pt2
# s=pd.Series(np.random.randn(1000))
# s=s.cumsum()
# sns.set()
#
# wykres = sns.relplot(kind='line', data=s, label='linia')
# wykres.fig.set_size_inches(7, 6)
# wykres.fig.suptitle('Wykres liniowy losowych danych')
# wykres.set_xlabels('indeksy')
# wykres.set_ylabels('wartości')
# wykres.add_legend()
# wykres.figure.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
# plt.show()

#Wykres kolumnowy
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],'Kontynent': ['Europa', 'Azja', 'AmerykaPołudniowa', 'Europa'],'Populacja': [11190846, 1303171035, 207847528, 38675467]}
# df = pd.DataFrame(data)
# sns.set()
# plot = sns.catplot(data=df, x='Kontynent', y='Populacja', kind='bar', ci=None, hue='Kontynent', estimator=np.sum,dodge=False, palette=['red', 'green', 'yellow'], legend_out=False)
# plot.fig.set_size_inches(7, 6)
# plot.add_legend(title='Populacja na kontynentach', loc='upper right')
# plot.fig.suptitle('Populacja na kontynentach')
# plot = sns.barplot(data=df, x='Kontynent', y='Populacja', ci=None, hue='Kontynent', estimator=np.sum,dodge=False, palette=['red', 'green', 'yellow'])
# plot.legend(title='Populacja na kontynentach')
# plot.set(title='Wykres słupkowy')
# plt.show()

#Wykres liniowy z wykorzystaniem ramki danych
# sns.set()
# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df)
# wykres=sns.lineplot(data=df,x=df.index,y='sepal length',hue='class',palette=['red','green','blue'])
# wykres.set_xlabel('indeksy')
# wykres.set_title('Wykres liniowy dancyh z Iris dataset')
# wykres.legend(title='Rodzaj kwiatu')
# plt.show()

# #Wykres punktowy
# sns.set()
# data={'a':np.arange(10),'c':np.random.randint(0,50,10),'d':np.random.randn(10)}
# data['b']=data['a']+10*np.random.randn(10)
# data['d']=np.abs(data['d'])*100
# print(data['c'])
# print(data['d'])
# df=pd.DataFrame(data)
# plot=sns.relplot(data=df,x="a",y="b",hue="c",palette='bright',size="d",legend=True)
# plot.fig.set_size_inches(6,6)
# plot.set(xticks=data['a'])
# plt.show()

#Wykres kolumnowy
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],'Kontynent': ['Europa', 'Azja', 'AmerykaPołudniowa', 'Europa'],'Populacja': [11190846, 1303171035, 207847528, 38675467]}
# df = pd.DataFrame(data)
# sns.set()
# # plot = sns.catplot(data=df, x='Kontynent', y='Populacja', kind='bar', ci=None, hue='Kontynent', estimator=np.sum,dodge=False, palette=['red', 'green', 'yellow'], legend_out=False)
# # plot.fig.set_size_inches(7, 6)
# # plot.fig.suptitle('Populacja na kontynentach')
# #plot.add_legend(title='Populacja na kontynentach')
# plot = sns.barplot(data=df, x='Kontynent', y='Populacja', ci=None, hue='Kontynent', estimator=np.sum,dodge=False, palette=['red', 'green', 'yellow'])
# plot.legend(title='Populacja na kontynentach')
# plot.set(title='Wykres słupkowy')
# plt.show()

#Wykres liniowy pandas
# ts=pd.Series(np.random.randn(1000))
# ts=ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()

#Wykres kolumnowy z Pandas DataFrame
# data={'Kraj':['Belgia','Indie','Brazylia','Polska'],
#       'Stolica':['Bruksela','New Delhi','Brasilia','Warszawa'],
#       'Kontynent':['Europa','Azja','Ameryka Południowa','Europa'],
#       'Populacja':[11190846,1303171035,207847528,38675467]}
# df=pd.DataFrame(data)
# print(df)
# grupa=df.groupby(['Kontynent']).agg({'Populacja':['sum']})
# print(grupa)
# wykres=grupa.plot.bar()
# wykres.set_ylabel("M1d")
# wykres.set_xlabel('Kontynent')
# wykres.tick_params(axis='x',labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja z podziałem na kontynenty')
# plt.savefig('wykres.png')
# plt.show()

#czytywanie danych z pliku i wyswietlenie grupowanych wartosci
# df=pd.read_csv('dane.csv',header=0,sep=";",decimal=".")
# print(df)
# grupa=df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia':['sum']})
# grupa.plot(kind='pie',subplots=True,autopct='%.2f%%',fontsize=20,figsize=(6,6),colors=['dodgerblue','darkorange'])
# plt.legend(loc='lower right')
# plt.title('Suma zamowienia dla sprzedawcy')
# plt.show()
#Zadanie 1
df=pd.read_excel('imiona.xlsx',header=0)
print(df)

# grupa=df.groupby(['Rok']).agg({'Liczba':['sum']})
# grupa.plot()
# plt.ylabel('Liczba urodzeń')
# plt.xlabel('Lata')
# plt.title('Wykres liczby urodzeń')
# plt.show()

grupa=df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres=grupa.plot(kind='bar',colors=['green','blue'])
wykres.set_xlabel('M i K')
wykres.set_ylabel("M1d")
wykres.tick_params(axis='x',labelrotation=0)
wykres.legend()
wykres.set_title('Ilosc urdzonych chlopow i bab')
plt.savefig('wykres1.png')
plt.show()

