import  random
x=int(input("wprowadz liczbe:"))
zestaw1=[]
while x>0:
    zestaw1.append(random.randrange(1,11))
    x-=1
    print(zestaw1)
zestaw2=[]
m = int(input("wprowadz liczbe:"))
for  i in range(m):
    zestaw2.append(random.randrange(4, 16))
print(zestaw2)
t=int(input("jaka liczba  Pan/Pani szuka?"))
if t in zestaw1:
    print("liczba z zestaw 1")
elif t in zestaw2:
    print("liczba jest z zestaw 2 ")
else:
    print("nie ma tej liczbe w zestafach")