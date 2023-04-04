import math
import random


#zadanie 1

with open("zadanie2.txt","r",encoding="windows-1250")as f:
    text=f.read()
    znaki=text[71:110]
print(znaki)
ilosc_a=znaki.count('A')

if ilosc_a>0:
    print("Tyle jest a:",ilosc_a)
else:
    print("nima")

#zadanie 2

lista=[1,2,3,4,5,6,7,2.5,2.7,2.9]

lista1=[x for x in lista if type(x)==float]
print(lista1)

#zadanie 3

lista11=[1,2,3,4,5,6,7,2.9,2.7,2.5]

def suma(lista11):
    pierwszy=lista11[0]
    nowa=[pierwszy+x for x in lista11]
    lista11.extend(nowa)
    return lista11


listy=suma(lista11)

print(listy)

#zadanie 4

rozwiazanie=pow(math.sin(56),2)+pow((pow(4,2))/(25)+math.log(85,3),1/4)
print(round(rozwiazanie,2))

#zadanie 5

#try:
 #   n = int(input("Podaj liczbę całkowitą n: "))
#except ValueError:
  #  print("Podane wartości muszą być liczbami całkowitymi!")
#else:
   # suma=0
   # for i in range(n+1):
   #     suma+=i

#with open("zadanie5.txt","w")as fil:
  #  fil.write(str(suma))


#zadanie1

#try:
 #   a=int(input("Podaj a:"))
  #  b=int(input("podaj b:"))
#except ValueError:
 #   print("podano liczbe ktora nie jest calkowita")
#else:
 #   suma=a**2+a*b+b**2
  #  with open("Zadanie11.txt","w")as wynik:
   #     wynik.write(str(suma))


#Zadanie 2
lis=[1,2,3,4,5,6]
lis2=[2,3,4,5,6,7]
lis3=[]
for i in range(len(lis)):
    lis3.append(lis[i]+lis2[i])

print(lis3)
#Zadanie 4

with open("Zadanie2.txt","r",encoding="windows-1250")as tul:
    text=tul.read()
    znaki=text[100:135]
print(znaki)
duze_litery=[c for c in znaki if c.isupper()]
if duze_litery:
    print("duze litery to sa",duze_litery)
    print("tyle o",len(duze_litery))
else:
    print("brak w sumie")


lista =[1,2,3,4,5,6,7]

a=3

lista3=[x for x in lista if x>a]
print(lista3)


sumar=pow(pow(math.e,3)+pow(math.cos(39),2),1/5)+pow(2/7,3)+math.pi
print(round(sumar,2))


lista=[]
i=0
for i in range(10):
    a=random.randint(0,30)
    lista.append(a)



with open("lista.txt","w")as kutas:
    text=kutas.write(str(lista))


with open("lista.txt","r")as kutes:
    text1=kutes.read()

print(text1)


import math


# slownik = {'mleko': 'sztuki', 'ziemiaki': 'kg', 'jogurt': 'sztuki'}
# lista = [key for key in slownik.keys() if slownik[key] == 'sztuki']
# print(lista)

# def trojkat_prostokatny(a, b, c):
#     if a**2 + b**2 == c**2:
#         return 'trójtkąt prostokątny'
#     else:
#         return 'trójkąt nie jest prostokątny'
# print(trojkat_prostokatny(3, 4, 5))

# def pole_trapezu(a=6,b=3,h=5):
#     return (a+b)*h/2
# print(pole_trapezu())

# def iloczyn(a=1, b=4, ile=10):
#     licznik = 0
#     while licznik != ile:
#         a *= b
#         licznik += 1
#     return a
# print(iloczyn())
# #
# #
# def iloczyn2(*liczby):
#     if len(liczby) == 3:
#         licznik = 0
#         wynik = liczby[0]
#         while licznik != liczby[2]:
#             wynik *= liczby[1]
#             licznik += 1
#         return wynik
#     else:
#         return 'zła ilość liczb wejściowych'
#
# print(iloczyn2(1,4,10))
#
# def iloczyn2(*liczby, b):
#     if len(liczby) == 0:
#         return 0
#     else:
#         iloczyn_liczb = liczby[0] * b
#         licznik = 1
#         while licznik != len(liczby):
#             iloczyn_liczb *= b
#             licznik += 1
#         return iloczyn_liczb
# print(iloczyn2(1,2,3,4,5,6,7,8,9,10,b=4))

# def lista_zakupow(** rzeczy):
#     koszt_zakupow = 0
#     for koszt in rzeczy:
#         koszt_zakupow += rzeczy[koszt]
#     return len(rzeczy), round(koszt_zakupow, 2)
# print(lista_zakupow(mleko=2.78, czekolada=5.40, kawa=22.99))

# a = input('podaj liczbę: ')
# try:
#     a = float(a)
#     pierwiastek = math.sqrt(a)
#     print(pierwiastek)
# except ValueError:
#     if type(a) != float:
#         print('nie wczytano liczby')
#     elif a < 0:
#         print('liczba a nie może być mniejsza od 0')





# plik = open('zad1.txt', 'w+')
# for b in a:
#     plik.write(str(b))
#     # plik.write('\n')
# plik.seek(0)
# zawartosc = plik.readlines()
# plik.close()
# print(zawartosc)



lista1=[]
i=0
for i in range(1,10):
    a=random.randint(0,100)
    lista1.append(a)

print(lista1)
lista2=[x for x in lista1 if x%2==0]
print(lista2)


def trojkat(aa,bb,cc):
    if (aa*aa)+(bb*bb)==(cc*cc):
        return "trojkat jest prostokatny"
    else:
        return "trojkat to nie jest"

sumadsad=trojkat(3,6,5)
print(sumadsad)

essas=math.sqrt(-1)
print(essas)