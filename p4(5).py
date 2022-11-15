import random
punkty=[]
#for i in range(15):
#    z=round(random.uniform(0, 50),2)
#    punkty.append(z)
punkty=[round(random.uniform(0, 50),2) for i in range(15)]
print(punkty)
print("Maks liczba:",max(punkty))
print("min liczba:", min(punkty))
c=float(input("wprowadz liczbe:"))
if c in punkty :
    print(punkty.index(c))
else:
    print ("niema tej liczby")
x=sum(punkty)
v=x/15
print("Srednie:",x/15)

lista1=[]
for p in punkty:
    if p <v:
        lista1.append(p)
print(len(lista1))
print(lista1)
lista2 (p for p in punkty if p>v)
print(len(lista2))
print(lista2)
