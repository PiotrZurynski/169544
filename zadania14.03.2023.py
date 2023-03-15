import math

print(math.e)
print(pow(math.e,10))
print(pow((math.log(5+(math.sin(8)*math.sin(8)))),1/6))

print(math.floor(3.55))
print(math.ceil(4.80))

imie ="PIOTR "
nazwisko ="Zurynski"

print(imie.capitalize()+ nazwisko.capitalize())

txt ="la la la potem jeszcze la i na koniec jeszcze la"
print('La powtorzylo sie:', txt.count('la'))

dowolnazmienna ="dowolna zmienna"
drugi=dowolnazmienna[2]
ostatni = dowolnazmienna[-1]
print("ostatni: %s" % ostatni)
print("drugi: %s" % drugi)

x=dowolnazmienna.split()
print(x)

x="string"
y=float(50)
z=hex(200)
print(x)
print(y)
print(z)
print(type(x),type(y),type(z))

listasportow=['spanie','granie','jedzenie','bieganie']
print(listasportow)
listasportow.reverse()
print(listasportow)
listasportow.extend(('wstawaniezlozka','rzutoszczepem'))
print(listasportow)

mojslowniczek={'wp':'wirtualnapolska','www':'worldwibeweb','gg':'gadugadu','ok':'okej'}
print(mojslowniczek['wp'])

slownikdogier = {'akcji':['gta','wiedzmin','rdr2','farcry',],'multiplayer':['lol','dota','overwatch','valorant'],'survival':['raft','minecraft','ark','strandeddeep']}
print(slownikdogier['akcji'])
kategorie=len(slownikdogier)
print("ilosc kategorii:%s"% kategorie)

print("Elementy w słowniku=",sum(len(v) for v in slownikdogier.values()))

print("Napisz cos dzieki")
#a=input('')
#print(a.count('a'))


#a=int(input())
#b=int(input())
#c=int(input())

#if(a>b and a>c):
    #print("a jest wieksze od b i c")
#elif(b>a and b>c):
    #print("b jest wieksze od a i c")
#elif(c>a and c>b):
    #print("c jest wieksze od a i b")

listadopotegi=[1.5,2.5,3.5,5,7,9,10]

for x in listadopotegi:
    print(x*x)
lista=list()
ii=0
while ii<10:
    aa = int(input())
    if aa % 2 == 0:
        lista.append(aa)
    ii += 1
print(lista)



