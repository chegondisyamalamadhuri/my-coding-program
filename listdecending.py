n=int(input())
a=list(map(int,input().split()))
for i in range(0,n-1):
    for j in range(i+1,n):
        if a[i]<a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
print(a)
