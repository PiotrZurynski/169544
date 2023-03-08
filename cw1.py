import sys

print(sys.version)

#print(5)
#print("nic")
#fruits =["apple","bananas","grapes"]
#for x in fruits:
   # print(x)


#i=1
#while i<=6:
    #print(i)
    #i+=1

#a="""nicnicninicnicninciicniadkksadlsakdlsa dsladlsaldksa dsadlksaldksakdlskaldkasld"""
#print(a)
#print(len(a))

a = 'napis'
print(type(a))
b=5
print(a+ str(b))
c=8
d=3
e=c+d
print(e)
print(type(e))
f=2+3j
print(f)
print(type(f))
print(c-d)
print(c//d)
print(c % d)
print(c**d)
print(pow(c,d))
print(2**(1/2))
print(c+2)
c +=2
print(c)
c*=2
print(c)
listy=[5,4,3,2,5,6,4,3]
print(listy)
listy.append(4)
print(listy)
listy.insert(1,299)
print(listy)
listy.pop(3)
print(listy)
listy.remove(4)
print(listy)
lista2=[5,4,3,2,1,6]
listy.extend(lista2)
print(listy)
listy.reverse()
print(listy)
listy.sort()
print(listy)

slownik = {1: 'a',2:2,3:'klucz',1:3}
print(slownik)

#print(slownik[2])
#slownik['nowy']='wartosc'
#print(slownik)

#slownik.pop(2)
#print(slownik)
#del slownik['nowy']
#print(slownik)

#print(slownik.keys())
#print(slownik.values())

#print('a= %(zm)d'%{'zm':12})
#print('a={}'.format(12))

#napis=input('wprowadz liczbe:')
#print(napis)
#print(type(napis))
#napis=int(napis)
#print(type(napis))

#instrukcja warunkowa
#if warunek:
    #instrukcja
#elif warunek
    #instrukcja
#else warunek:
    #instrukcja


#a=input('podaj a:')
#b=input('podaj b:')
#c=input('podaj c:')
#d=input('podaj d:')
#a=int(a)
#b=int(b)
#c=int(c)
#d=int(d)
#if a>b:
    #print("A wieksze od b")
#elif a<b:
    #print("A mniejsze od b")
#else:
   #print("Obie liczby sa rowne")

#if(a>b)&(c>d):
    #print('A wieksze od b i c wieksze od d')
#else:
    #print(' A nie jest wieksze od b lub c nie jest wieksze od d')



#for element in sekwencja:
    #instrukcja
#else:
    #instrukcje po petli

for x in range(1,6,1):
    print(x)
else:
    print("koniec petli for")


lista=[1,2,3,4,5,6,7,8,8,10]

#for x in lista:
   # print(x)

#for lista in range(0,11,1):
   # print(lista)

#while warunek:
    #instrukcja
#else:
    #instrukcja


#licznik=0
#while licznik != len(lista):
    #print(lista[licznik])
    #licznik += 1

#liczby =[2,5,6,7,3,4]
#a=input('podaj a:')
#a=int(a)
#licznik=0

#while licznik != len(liczby):
   # if liczby[licznik]-a == 0:
        #print(str(a) + '-' + str(liczby[licznik]+' = 0'))
    #licznik += 1



liczba = [ 2,2,2,2,4,2,5,6,7,2,1,3 ]

a=2
i =0
while i != len(liczba):
    if liczba[i] == a:
        liczba.pop(i)
        i -= 1
    i +=1
print(liczba)








