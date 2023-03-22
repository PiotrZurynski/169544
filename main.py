import random
encoding ='utf8'
#Zadanie1
plik=open("dane.txt")

lista1=[]
i=0
for i in range(10):
    a = random.randint(0, 30)
    lista1.append(a)
    i+=1
lista2=[]
for j in lista1:
    lista2.append(j*2)

print(lista1)
print(lista2)
plik= open('dane.txt','w')
plik.writelines(str(lista2))
plik.close()

#zadanie 2
plik=open("dane.txt","r")
znaki=plik.read(100)
linia=plik.readline()
wiersze=plik.readlines()
print(znaki)
#zadanie 3
with open("text.txt", "r+") as text:
    text.write("Hello World!!!\nNew World\nOld World")
with open("text.txt") as text:
    dane = text.read()
print(dane)

#zadanie 4

class nazakupy:
    "Przechowuje chyba liste zakupow"
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jednostkowa):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jednostkowa=cena_jednostkowa

    def wyswietl_produkt(self):
        print(f"Produkt:{self.nazwa_produktu},ilosc:{self.ilosc},jednostka_miary:{self.jednostka_miary},cena:{self.cena_jednostkowa} zł")
    def ile_produktu(self):
        return f"{self.ilosc} {self.jednostka_miary}"
    def ile_kosztuje(self):
        return self.ilosc*self.cena_jednostkowa


ziemniaki=nazakupy("ziemniaki",3,"kg",2)
ziemniaki.wyswietl_produkt()
print(ziemniaki.ile_produktu())
print(ziemniaki.ile_kosztuje())

class ciag:
    "Klasa do definicji ciagow arytmetycznych"
    def __init__(self,wyswietl_dane,pobierz_elementy,pobierz_parametry,policz_sume,policz_elementy):
        self.wyswietl_dane=wyswietl_dane
        self.pobierz_elementy=pobierz_elementy
        self.pobierz_parametry=pobierz_parametry
        self.policz_sume=policz_sume
        self.policz_elementy=policz_elementy

    def wezdajmicos(self):
        pierwszyelement=input("Podaj 1 element ciagu:")
        roznica=input("Podaj roznice ciagu:")
        iloscelementow=input("Podaj ilosc elementow ciagu")

    def suma(self):
        return (self.wezdajmicos.pierwszyelement*self.wezdajmicos.iloscelementow)/2













