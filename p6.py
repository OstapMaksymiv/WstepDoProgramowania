n=int(input("ile studentow\n"))
t=n
s=0
while n>0:
    k=int(input("wprowadz punkt"))
    s=s+k
    n-=1
print("sred:",s/t)