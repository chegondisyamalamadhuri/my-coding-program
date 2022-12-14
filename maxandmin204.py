l=[]
n=int(input("enter n value"))
l=list(map(int,input().split()))
maxi=l[0]
mini=l[0]
for i in range(1,n):
    if l[i]>maxi:
        maxi=l[i]
    else:
        mini=l[i]
print(maxi)
print(mini)
