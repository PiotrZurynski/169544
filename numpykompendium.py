import numpy as np

#inicjalizacja tablicy
a=np.array([[0,1],[2,3]])
print(a)

#drugi sposob
a=np.arange(2,5,0.1)
print(a)

#wypisanie typu zmiennej tablicy(nie jej elementow)
print(type(a))

#sprawdzenie typu danych tablicy
print(a.dtype)

#inicjalizacja tablicy z konkretnym typem danych
a=np.arange(2,dtype='int64')
print(a.dtype)
print(a)

#Zapisywanie kopii tablicy jako tablicy z innym typem
b=a.astype('float')
print(b)
print(b.dtype)

#wypisanie rozmiaru tablicy
print(b.shape)

#mozna tez sprawdzic ilosc wymiarow tablicy
print(a.ndim)

#stworzenie tablicy wielowymiarowej moze wygladac tak
#parametrem przekazywanym do funkcji array jest obiekt
#moze to byc pythonowa lista
m=np.array([np.arange(2),np.arange(2)])
print(m.shape)

#ponownie typem jest ndarray
print(type(m))

zera=np.zeros((5,5))
print(zera)
jedynki=np.ones((4,4))
print(jedynki)

#warto sprawdzic jaki jest domyslny typ danych takich tablic
print(zera.dtype)
print(jedynki.dtype)

#mozna rowniez stworzyc pusta macierz o podanych wymiarach
#wartosci umieszczane sa losowe najpierw podawana jest icos
pusta=np.empty((2,2))
print(pusta)


macierz=np.array([[12,11],[2,1]])
print(macierz)
## do elementow tablicy mozemy odwolac sie tak jak do elementow ...
poz_1=macierz[1,0]
poz_2=macierz[0][0]
print(poz_1)
print(poz_2)
#tworzenie macierzy 2x2 wraz z uzupelnieniem
#macierz=np.array([[12,11],[2,1]])

liczby=np.arange(1,2,0.1)
print(liczby)
#podobnie dziala funkcja linspace ktore dzialanie jest
liczby_lin=np.linspace(1,2,5,endpoint=False)
print(liczby_lin)
# a teraz mozemy utworzyc dwie macierze najpierw wartosci

z=np.indices((5,3))
print(z)
print(z[0][4][2])
#podobnie jak w matlabie mozemy tworzyc macierz diagonalna
mat_diag=np.diag([a for a in range(5)])
print(mat_diag)
#w powyzszym przykladzie stworzony wektor wartosci zostan
#mozemy podac drugi paramter funkcji diag, ktory okresla
#ktora zostanie wypelniona wartosciami podanego wektora
mat_diag_k=np.diag([a for a in range(5)],-1)
print(mat_diag_k)

#numpy jest wstanie stworzyc tablice jednowymiarowa z dowo
z=np.fromiter(range(7),dtype='int32')
print(z)

znaki=b'ogolna'
z1=np.frombuffer(znaki,dtype='S1')
print(z1)

z2=np.frombuffer(znaki,dtype='S2')
print(z2)

znaki='ogolna'
z3=np.array(list(znaki))
z4=np.array(list(znaki),dtype='S1')
z5=np.array(list(b'ogolna'))
z6=np.fromiter(znaki,dtype='S1')
print(z3)
print(z4)
print(z5)
print(z6)


a=np.arange(10)
print(a)
s=slice(2,7,2)
print(a[s])
#mozemy ciac tablice rowniez w sposob znany z ciecia list

print(a[2:7:2])
#lub tak
print(a[1:])
print(a[2:5])
print('aaaaaa')
#w podobny sposob postepujemy w przypadku tablic wielowymiarowych
mat=np.arange(25)
#teraz zmieniamy kształt tablicy jednowymiarowej na macierzy
mat=mat.reshape((5,5))
print(mat)
print('aaaaaa')
print(mat[1:])#od drugiego wiersza
print('aaaaaa')
print(mat[:,1:2])#druga kolumna jako wektor
print('aaaaaa')
print(mat[:,4:5])#ostatnia kolumna
print('aaaaaa')
print(mat[2:5,1:3])#2i3 kolumna dla 3,4,5 wierszy
print('aaaaaa')
print(mat[:,range(2,6,2)])#3 i 5 kolumna
print(mat[:,[2,4]])

x=np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print(x)
rows=np.array([[0,0],[3,3]])
cols=np.array([[0,2],[0,2]])
y=x[rows,cols]
print(y)




