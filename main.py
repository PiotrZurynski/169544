import numpy as np

a=np.array([10,20,30,40])
b=np.arange(4)
print(a)
print(b)
print(a+b)

print(pow(a,b))
print(np.sin(a))
print(np.sin(b))


d=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(d)
print(d.sum())
print(d.sum(axis=0))
print(d.sum(axis=1))
print(d.cumsum(axis=1))

a=np.array([[2,1,3],[-1,2,4]])
b=np.array([[1,3],[2,-2],[-1,4]])

c=np.dot(a,b)
print(c)
d=a.dot(b)
print(d)


a=np.arange(6).reshape((3,2))
print(a)
for b in a:
    print(b)

for c in range(0,a.shape[0],1):
    for d in range(0,a.shape[1]):
        print(a[c][d])


for c in a.flat:
    print(c)

a=np.arange(6)

print(a)


print(a.shape)

b=a.reshape((2,3))
print(b)
print(b.shape)

c=a.reshape((3,2))
print(c)
print(c.shape)


d=a.reshape((6,1))
print(d)
print(d.shape)

e=c.ravel()
print(e)
print("")
print(c)
f=c.T
print(f)
print(f.shape)


print("")
print("")
print("")
print("")
print("")
print("")


a=np.array([0,1,2])

b=np.array([0,1,2])
c=a.dot(b)
print(c)
d=a*b
print(d)

#Zadanie 1
a=np.array([1,2,3])
b=np.array([2,3,4])
c=a.dot(b)
print(c)
#Zadanie 2
print("")
b=np.array([[1,3,3],[2,-2,3],[-1,4,3]])
c=np.array([[4,5,6,7],[5,6,7,8],[6,7,8,9],[7,8,9,10]])
print(b)
print("")
print(c)

najmniejsza=np.min(b,axis=1)
najmniejsza1=np.min(b,axis=0)

print(najmniejsza,najmniejsza1)

najmniejsza=np.min(c,axis=1)
najmniejsza1=np.min(c,axis=0)
print(najmniejsza,najmniejsza1)
print("")
#Zadanie3

a=np.array([1,2,3])
b=np.array([2,3,4])
c=a.dot(b)
print(c)
print("")
#Zadanie4
a=np.array([1,2,3])
b=np.array([2.5,3.5,4.5])
c=a*b
print(c)
print("")

#Zadanie 5
a=np.array([[1,2,3],[2,3,4]])
print(a)
a1=np.sin(a)
print(a1)
print("")
#Zadanie 6
b=np.array([[1,2,3],[2,3,4]])
print(b)
b1=np.cos(b)
print(b1)
print("")
#zaadnie 7
d=a+b
print(d.sum())
print("")
#zadanie 8
a=np.arange(9).reshape((3,3))
for b in a:
    print(b)

#Zadanie 9