print("Jaką operację chcesz wykonać?\n1) dodawanie\n2) odejmowanie\n3) mnożenie\n4) dzielenie\n5) potęgowanie")
c=str(input("Wpisz numer operacji"))
try:
    a=float(input("Podaj argument 1"))
except:
    print("Podana wartosc nie jest liczba")
    exit()
try:
    b=float(input("Podaj argument 2:"))
except:
    print("Podana wartosc nie jest liczba")
    exit()
if c=="1":
    print(a+b)
elif c=="2":
    print(a-b)
elif c=="3":
    print(a*b)
elif c == "4":
    if (a / b):
     print (a / b)
    elif b==0:
        print("to jest blad")



elif c == "5":
    print(a**b)
else:
    print("Brak operacji o podanym nomeru")