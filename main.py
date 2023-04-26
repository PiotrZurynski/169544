import numpy as np
import pandas as pd

#Series
s=pd.Series([1,3,5,np.nan,6,8])
print(s)
#Wypisanie od indexu 0 do 5 liczb w tym np.nan ktory jest indexem 3


s=pd.Series([10,12,8,14],index=['a','b','c','d'])
print(s)
#podmianka indexu zamiast od 0 do 3 to od a do d


#DataFrame
#tworzenie dataframe na podstawie słownika
data={'Kraj':['Belgia','Indie','Brazylia'],'Stolica':['Bruksela',"New Delhi",'Brasilia'],'Populacja':[11190846,1303171035,207847528]}
df=pd.DataFrame(data)
print(df)
#Stworzenie tabelki kraj,stolica populacja indeksy od 0 do 2

print("")

#DataFrame przechowuje typ dla każdej kolumny co możemy sprawdzić wpisując
print(df.dtypes)
#dtype:object


print("")
#Możemy również w prosty sposob stworzyć serię danych - czyli probki dla kolejnych #dat,pomiarów czasu
daty=pd.date_range('20210324',periods=5)
print(daty)
#wyswietlilo daty od 2021-03-24 do 2021-03-28

print("")
df=pd.DataFrame(np.random.randn(5,4),index=daty,columns=list('ABCD'))
print(df)

print("")

#Biblioteka Pandas umożliwia również tworzenie DataFrame'ów z zewnętrznych źródeł danych
#CSV, odczyt i zapis
df=pd.read_csv('australian.txt',header=None,sep=' ',decimal='.')
print(df)
df.to_csv('plik.csv',index=True)

print("")

#Excel-wymagana jest biblioteka openpyxl

xlsx=pd.ExcelFile('Wyniki.xlsx')
df=pd.read_excel(xlsx,header=0)
print(df)
df.to_excel('Wyniki.xlsx',sheet_name='arkusz_pierwszy')


print("")
s=pd.Series([10,12,8,14],index=['a','b','c','d'])
print(s)
print("")
data={'Kraj':['Belgia','Indie','Brazylia'],'Stolica':['Bruksela',"New Delhi",'Brasilia'],'Populacja':[11190846,1303171035,207847528]}
df=pd.DataFrame(data)
print(df)
print("")
#pojedynczy element serii, odnosimy sie do nazwy indeksu
print(s['c'])
#wyswietla wartosc o indexie c czyli druga wartosc
print("")
#mozemy rowniez dostac sie do wartosci serii jak do pola klasy
print(s.c)
print("")
#pojedynczy element ramki danych, tak jak przy cieciu tablic,oparte na indeksach
print(df[0:1])
print("")
#kolumna po etykiecie
print(df['Populacja'])
print("")
#pobieranie pojedynczej wartosci po indeksie wiersza i kolumny
print(df.iloc[0,0])
#wyswietlilo napis Belgia
print("")
#pobieranie wartosci po indeksie wiersza i etykiecie kolumny
print(df.loc[0,"Kraj"])
print(df.at[0,"Kraj"])
#wyswietlenie napisu Beliga w obu przypadkach strzalka w gore
print("")
#podobnie jak w przypadku serii można odwoływać się do kolumn jak do pól klasy
#dodatkowo print jest wywoływany jak w pętli dla każdego elementu danej kolumny
print('Kraj:'+df.Kraj)
#wyswietla to po indeksach kraje indeks 0 kraj:belgia itd

#Pandas posiada rowniez funkcje pozwalajace na losowe pobieranie elementow lub w odniesieniu do procentowej wielkosci calego zbioru
#jeden losowy element
print("")
print(df.sample(1))
#srednio to wyswietla losowe elementy do () wyswietla belgie czyli pierwsza wartosc a dla 2 belgie i brazylie dla 1 tylko indie

print("")
#ilosc elementow procentowo uwaga na zaokraglenia
print(df.sample(frac=0.5))

#jezeli potrzeba weicej probek niz znajduja siew  zbiorze i dopuszczamy duplikaty to mozemy uzyc replace ktory bedzie losowal powtorzeniami
print("")
print(df.sample(n=10,replace=True))
#zamiast wyswietlac cala kolekcje mozna wyswietlac okreslona ilosc elementow od poczatku kolekcji
#lub od jej konca
print("")
print(df.head()) #cala kolekcja
print(df.head(2))#2 rzeczy w kolekcji zamiast 3
print(df.tail(1))#wyswietlenie ostatniego elementu kolekcji

#Pandas jest tez wstaie wyswietlic statystyke dla wartosci ktore dana kolekcja zawiera o ile sa jakeis kolumny z danymi numerycznymi

print("")
print(df.describe())#ciezko powiedziec co te wyniki znacza ale ok
#transpozycja kolekcji
print("")
print(df.T)#fajna

print("")
print("")
#wyswietla indeksy zamiast od 0 do 3 to od a do d
s=pd.Series([10,12,8,14],index=['a','b','c','d'])
print(s)
print("")
#wyswietla dane z serii gdzie wartosc wieksza od 9
print(s[(s>9)])
print("")
#Nieco inny efekt mozna osiagnac wykorzystujac funkcje where ktora zwraca kolekcje w oryginalnej wielkosci
#(liczebnosc) elementow ale wartosci nie spelniajace warunku uzupelnia wartoscia null

print(s.where(s>10))
#Mozemy tez podac wartosc kotra zostanie zastapiona przez NaN
print(s.where(s>10,'zamale'))
#jeszcze inna wlasnosc where pozwala na modyfikowanie oryginalnego zbioru (domyslnie zwracanie jest kopia)
seria=s.copy()
seria.where(seria>10,'za male',inplace=True)
print("#######")
print(seria)
#wyswietla dane z serii gdzie wartosc nie jestwieksza od 10
print("")
print(s[~(s>10)]) #logicznie zanegowane poprostu
print(s[(s<13)&(s>8)])#warunki zwykle ja to logike znam
#warunku dla pobierania DataFrame
print(df[df['Populacja']>1200000000])
print(df[(df.Populacja>1000000)&(df.index.isin([0,2]))])
#inny przyklad z lista dopuszczalnych wartosci oraz isin zwracajaca wartosci boolowskie
print("")
szukaj=['Belgia','Brasilia']
print(df.isin(szukaj))

#zamiana usuwanie i dodawanie danych
#w przypadku serii mozemy dodawac zmienachwartosci poprzez  odwolanie sie do elementu z serii przez klucz indeks
s['e']=15
print(s.e)
s['f']=16
print(s)
#podobnie dla DataFrame manieco inny efekt -wartosc ustawiona dla wszystkich kolumn
df.loc[3]='dodane'
print(df)
df.loc[4]=['Polska','Warszawa',38000000]
print(df)
#usuwanie danych mozna wykonac przez funkcje drop jak w sql ale pamietajmy ze operacja nie wykonuje sie in-place wiec zwracana bedzie kopia DataFrame z usunietymi wartosciami
new_df=df.drop([3])
print(new_df)
#wiec jesli chcemy zmienic pierwotny zbior dodajemy parametr inplace=true
df.drop([3],inplace=True)
print(df)
#mozna usuwac rowniez cale kolumny po nazwie indeksu ale wykonanie tej komendy uniemozliwi
#wykonanie dalszego kodu mozna przetestowac po zakomentowaniudalszej czesci listingu
#df.drop('Kraj',axis=1,inplace=True)
#Do data Frame mozemy dodawac rowneiz kolumny zamiast wierszy
df['Kontynent']=['Europa','Azja','Ameryka Południowa','Europa']
print(df)
#Pandas ma rowniez wlasne funkcje sortowania mądre osoby to wymysliły!
print(df.sort_values(by='Kraj'))
#grupowanie
grouped=df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))
#można tez jakw sql czy excelu uruchomic funkcje agregujace na danej kolumnie
print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))
#posumowalo fajnie

#Zadanie 1
xlsx=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(xlsx,header=0)
print(df)

print(df[df['Liczba']>1000])

xlsx=pd.ExcelFile('imiona.xlsx',sheet_name='Imie')
marcin_df=imio