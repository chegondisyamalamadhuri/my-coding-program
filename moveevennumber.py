n=int(input())
ol=list(map(int,input().split()))
nl=[]
zl=[]
for i in range(0,n):
    if ol[i]%2==0:
        nl.append(ol[i])
    else:
        zl.append(ol[i])
l=nl+zl
for i in range(n):
    print(l[i],end=' ')
