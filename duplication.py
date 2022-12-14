n=int(input())
flag=0
a=list(map(int,input().split()))
for i in range(0,n-1):
    for j in range(i+1,n):
        if a[i]==a[j]:
            flag=0
            print('yes')
            break
        else:
            if flag==1:
                print('no')
