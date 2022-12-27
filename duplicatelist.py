n=int(input())
l=list(map(int,input().split()))
x=int(input())
k=0
for i in range(0,len(l)):
    if(l[i]==x):
        print(i,end=" ")
        k=1
if(k==0):
    print(-1)
