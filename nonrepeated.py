n=int(input())
l=list(map(int,input().split()))
res=[]
for i in range(0,n):
    count=0
    for j in range(0,n):
        if l[i]==l[j]:
            count=count+1
    if count==1:
        res.append(l[i])
res.sort()
print(res)
