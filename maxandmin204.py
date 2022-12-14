l=[]
n=int(input("enter n value"))
l=list(map(int,input().split()))
max=l[0]
min=l[0]
for i in range(1,n):
    if l[i]>max:
        max=l[i]
    else:
        min=l[i]
print(max)
print(min)
