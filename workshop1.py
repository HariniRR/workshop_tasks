a=list(input("enter an array").split())
b=int(input("enter a number"))
c=0
for i in a:
    if a[i]<b:
        c+=1
print (c)
