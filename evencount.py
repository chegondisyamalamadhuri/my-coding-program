n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(0,n):
    if i%2==0:
        count=count+1
        
print(count)
