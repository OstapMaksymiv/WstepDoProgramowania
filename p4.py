x=str(input("wprowadz litere: "))
if len(x)>1 or len(x)==0:
    print("blad")
    exit()
if ord('A')<=ord(x)<=ord('Z'):
    print(chr (ord(x)+32))
elif ord('a') <= ord(x) <= ord('z'):
   print( chr (ord(x)-32))
else: print("to nie jest litera")