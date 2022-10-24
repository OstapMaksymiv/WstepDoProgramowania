print("Wprowadź wiek klienta: ")
x=int(input())
if x<4:
    print("bezplatne")
elif 4<=x<18:
    print("10 zl")
else:
    print("20 zl")