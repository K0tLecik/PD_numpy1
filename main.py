from numpy import *
from math import *

print("Zadanie 1: ")
a = arange(4,81,4)
print(a)

print("Zadanie 2: ")
a = arange(1,10,0.5)
print(a)
b = a.astype("int64")
print(b)
print(b.dtype)

print("Zadanie 3:")
def zad3(n):
    return arange(1,n*n+1).reshape((n,n))
print(zad3(5))

print("Zadanie 4:")
def zad4(x,y):
    a = logspace(1, y, num=y, base=x)
    print(a)
zad4(2,4)

print("Zadanie 5:")
def zad5(n):
    a = arange(n,0,-1)
    print(diag([x for x in a]))
zad5(5)

print("Zadanie 6:")

a = array(list('apel'))
b = array(list('azyl'))
c = array(list('lipa'))
c = flip(c)
x = zeros((4,4), dtype='str')
x = diag(b)
x[:,0] = a
x[0,:] = c
print(x)

print("Zadanie 7:")

def zad7(n):
    a = diag([2 for x in range(n)])
    for x in range(1, n):
        b = [2+(2*x) for y in range(n-x)]
        a = a + diag(b, x)
        a = a + diag(b, -x)
    print(a)
zad7(3)

print("Zadanie 8:")

def zad8(tab, kierunek):
    if (kierunek == 'poziomo'):
        if (tab.shape[0] % 2 != 0):
            print("Nie da rady")
        tab1 = tab[0:int(tab.shape[0]/2), :]
        tab2 = tab[int(tab.shape[0]/2), :]
        print(tab1,"\n\n",tab2)
    elif (kierunek == "pionowo"):
        if (tab.shape[1] % 2 != 0):
            print("Nie da rady")
        tab1 = tab[:, 0:int(tab.shape[1]/2)]
        tab2 = tab[:, int(tab.shape[1]/2):]
        print(tab1, "\n\n", tab2)

zad8(zad3(6), kierunek='pionowo')

print("Zadanie 9:")

def zad9(a,r):
    b = arange(a,a+25*r,r).reshape((5,5))
    return b
print(zad9(5,-2))