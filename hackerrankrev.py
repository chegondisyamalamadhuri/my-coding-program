n,m=input().split(" ")
arr=list(map(int,input().split()))
n=int(n)
m=int(m)
for i in range(0,m):
    first=arr[0]
    for j in range(0,n-1):
        arr[j]=arr[j+1]
    arr[n-1]=first
for i in arr:
    print(i,end=' ')
