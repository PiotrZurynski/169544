import random
#Zadanie1
a = [1-x for x in range(1,11)]
b = [4**i for i in range(8)]
c = [x for x in b if x%2 == 0]
print(a)
print(b)
print(c)
##Zadanie2

lista1=[]
i=0
for i in range(10):
    a = random.randint(0, 100)
    lista1.append(a)
    i+=1
print(lista1)

lista2=[j for j in lista1 if j%2==0]
print(lista2)
##Zadanie3
spozywka={'mleko':'sztuki','chleb':'sztuki','ser':'kg','ziemniaki':'kg','mieso':'kg'}
spozywka2 = {k:v for k,v in spozywka.items() if v =='sztuki'}
print(spozywka2)

##Zadanie4
def trojkatprostokatny(aa,bb,c):
       if aa**2 + bb**2==c**2:
           print("trojkat jest prostokanty")
       else:
            print("trojkat nie jest prostokatny")

trojkatprostokatny(8,15,17)
##Zadanie5
def poletrapezu(aaa=2,bbb=3,h=5):
    pole=((aaa+bbb)*h)/2
    return pole

print("poletrapezu:",poletrapezu())


##zadanie6
def ciagi(ae=1, be=4, ile=10):
    for i in range(ile):
        ae*=be

    return(ae)

print(ciagi())

#Zadanie7

def ciag(* liczby):
    if len(liczby)==0:
        at,bt,ilet=1,4,10
    elif len(liczby)== 1:
        at,bt,ilet=liczby[0],4,10
    elif len(liczby)==2:
        at,bt,ilet=liczby[0],liczby[1],10
    elif len(liczby)==3:
        at,bt,ilet=liczby
    else:
        raise TypeError("funkcja iloczynowa ma conajwyzej 3 wartosci")


    for i in range(ilet):
        at*=bt


    return at

print(ciag())
#Zadanie 8



#Zadanie 9
def pierwiastek(p):
    if p<0:
        print("co ty tu napisales takiego pierwiastka ci nei oblicze")
    elif p>=0:
        wynik=p**(1/2)

    return wynik

print(pierwiastek(0))





