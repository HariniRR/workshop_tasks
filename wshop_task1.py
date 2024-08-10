#num of elements in an array that are < a specific num 
#a=list(map(int(input("enter an array").split())))
a=list()
v=(int(input("enter an array").split()))
a.append(v)
print(a)
b=int(input("enter a number"))
c=0
for i in a:
    if a[i]<b:
        c+=1
print (c)
