import numpy as np
#Zadanie 1
a=np.arange(0,80,4)
print(a)

#Zadanie 2
b=np.arange(2,5,0.1)
print(b)
print(b.dtype)
b=np.arange(2,5,dtype='int32')
print(b.dtype)
print(b)


#Zadanie 3
def funkcja(n):
    tablica=np.zeros((n,n),dtype=np.int32)
    for i in range(n):
        for j in range(n):
            tablica[i][j]=2**(i+j)

    return tablica

n=5
wynik=funkcja(n)
print(wynik)

#Zadanie 4
def generuj(n,potega):
    funkcja=np.logspace(0,4)

