l=list(map(int,input().split()))
min=l[0]
max=l[0]
for i in range(0,len(l)):
    count=0
    for j in range(1,l[i]+1):
        if(l[i]%j==0):
            count+=1
    if(count==2):
        if(l[i]<min):
            min=l[i]
        if(l[i]>max):
            max=l[i]
print(min)
print(max)
