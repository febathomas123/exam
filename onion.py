n=input("enter the string")
c=n[0]
for i in n:
    if i==c:
        n=n.replace(i,'$')
        n=c+n[1:]
print(n)