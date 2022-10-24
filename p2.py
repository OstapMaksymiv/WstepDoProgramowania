st=str(input("enter letter\n"))
if len(st)>1 or len(st)==0:
    print("blad")
    exit()
if ord('A')<=ord(st)<=ord('Z'):
    print("Litera jest duza")
elif ord('a')<=ord(st)<=ord('z'):
   print("Litera jest mala")
else: print("to nie jest litera")