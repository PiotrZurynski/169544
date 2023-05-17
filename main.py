import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import math
import random

#plt.plot([1,3,5,7])
#plt.show()

#x=np.array([1,2,3,4])
#y=x**2
#plt.plot(x,y,'ko-')
#plt.axis([0,6,0,20])
#plt.show()

#plt.plot(x,y,'r')
#plt.plot(x,y,'o')
#plt.axis([0,6,0,20])
#plt.show()


#x=np.arange(0,5,0.2)
#plt.plot(x,x,'r--',x,x**2,'bo',x,x**3,'g^',)
#plt.legend(labels=['liniowa','kwadratowa','sześcienna'])
#plt.show()

#x=np.arange(0,5,0.2)
#plt.plot(x,x,'r--',label='liniowa')
#plt.plot(x,x**2,'bo',label='kwadratowa')
#plt.plot(x,x**3,'g^',label='sześcienna')
#plt.legend(loc='best')
#plt.show()


#x=np.arange(0,10.1,0.1)
#plt.plot(x,np.tan(x),'r-',label='sinus')
#plt.xlabel('wartosci x')
#plt.ylabel('wartosci y')
#plt.legend()
#plt.title('wykres liniowy funkcji sin(x)')
#plt.show()

#data={'a':np.arange(50),'c':np.random.randint(0,50,50),'d':np.random.randn(50)}

#data['b']=data['a']+10*np.random.randn(50)
#data['d']=np.abs(data['d'])*100
#plt.scatter('a','b',c='c',s='d',data=data,cmap='plasma')
#plt.xlabel('klucz a')
#plt.ylabel('klucz b')
#plt.show()

#x1=np.arange(0,2,0.02)
#x2=np.arange(0,2,0.02)

#y1=np.sin(x1*np.pi*2)
#y2=np.cos(x2*np.pi*2)

#plt.subplot(4,1,1)
#plt.plot(x1,y1)
#plt.title('Wykres sin(x1)')
#plt.xlabel('x')
#plt.ylabel('sin(x1)')
#plt.subplot(4,1,4)
#plt.plot(x2,y2,'r')
#plt.title('Wykres cos(x2)')
#plt.xlabel('x')
#plt.ylabel('cos(x2)')
#plt.subplots_adjust(hspace=0.5)
#plt.show()

#x1=np.arange(0,2,0.02)
#x2=np.arange(0,2,0.02)

#y1=np.sin(x1*np.pi*2)
#y2=np.cos(x2*np.pi*2)

#fig,axs=plt.subplots(3,2)
#axs[0,0].plot(x1,y1)
#axs[0,0].set_title('Wykres funkcji sinus')
#axs[0,0].set_xlabel('x')
#axs[0,0].set_ylabel('y')

#axs[1,1].plot(x2,y2,'k^')
#axs[1,1].set_title('Wykres funkcji cosinusa')
#axs[1,1].set_xlabel('x')
#axs[1,1].set_ylabel('y')

#axs[2,0].plot(x1,y1,'r--')
#axs[2,0].set_title('Wykres funkcji sinus')
#axs[2,0].set_xlabel('x')
#axs[2,0].set_ylabel('y')
#plt.subplots_adjust(hspace=0.7)
#fig.delaxes(axs[0,1])
#fig.delaxes(axs[1,0])
#fig.delaxes(axs[2,1])
#plt.show()

data={'Kraj':['Belgia','Indie','Brazylia','Polska'],'Stolica':['Bruksela','New Delhi','Brasilia','Warszawa'],'Kontynent':['Europa','Azja','Ameryka Południowa','Europa'],'Populacja':[11190846,1303171035,207847528,38675467]}
#df=pd.DataFrame(data)
#print(df)
#grupa=df.groupby('Kontynent')
#etykiety=list(grupa.groups.keys())
#wartosci=list(grupa.agg('Populacja').sum())

#plt.bar(x=etykiety,height=wartosci,color=['yellow','red','green'])
#plt.xlabel('Kontynenty')
#plt.ylabel('Populacja')

#plt.show()
#grupa=df.groupby('Kontynent').agg({'Populacja':['sum']})
#print(grupa)

#grupa.plot(kind='bar',xlabel='Kontynenty',ylabel='Populacja',
           #legend=True,rot=0,title='Populacja na kontynentach')
#plt.savefig('wykres.png')
#wykres=grupa.plot.bar()
#wykres.set_ylabel('Populacja')
#wykres.set_xlabel('Kontynenty')
#wykres.tick_params(axis='x',labelrotation=0)
#wykres.legend()
#wykres.set_title("Populacja na kontynentach")

#plt.show()


#ts=pd.Series(np.random.randn((1000)))
#ts=ts.cumsum()
#ts.plot()
#plt.show()

df=pd.read_csv('dane.csv',header=0,sep=';',decimal='.')
print(df)
grupa=df.groupby('Imie i nazwisko').agg({'Wartość zamówienia':['sum']})
grupa.plot(kind='pie',subplots=True,autopct='%.2f%',fontsize=20,figsize=(6,6),colors=['red','green'])
plt.legend(loc='lower right')
plt.title('Procent zamowienia dla sprzedazy')
plt.show()
