
zwierzeta=[]
y=0
while y<4:
    x = input("Dodaj nazwe zwiezat:\n")
    zwierzeta.append(x)
    y+=1
print(zwierzeta)
a=sorted(zwierzeta)
print(a)

print(zwierzeta[0],zwierzeta[-3:])
print(len(zwierzeta))