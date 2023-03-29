import random
import math
with open("tekst.txt","r",encoding='utf-8') as plik:
    txt=plik.read()

    znaki=txt[71:111]

    licz_a=znaki.count('e')
    if licz_a ==0:
        print("nie ma litery 'A'")
    else:
        print("Litera a wystepuje",licz_a)


lista=[1,2,3,4,4.5,5.5,6.6,8,9,10.5]
lista1=[x for x in lista if isinstance(x,float)]


print(lista)
print(lista1)
#Zadanie5
try:
    suma=0
    n=int(input("podaj liczbe"))
except:
    print("Bledne dane")
else:
    for i in range(n+1):
        suma+=i
        i+=1
print(suma)

with open("zadanie5.txt","w") as pliczek:
    pliczek.write(str(suma))

#Zadanie3

def funkcja(list):
    pierwsze=list[0]
    nowalista=[pierwsze+x for x in list]
    nowalista.extend([pierwsze+sum(list)])
    return nowalista

list=[1,2,3]
a=funkcja(list)
print(a)






#Zadanie3

aa=pow(math.sin(56),2)+pow(((pow(4,2)/25)+(math.log(85,3))),1/4)
bb=round(aa,2)
print(bb)















