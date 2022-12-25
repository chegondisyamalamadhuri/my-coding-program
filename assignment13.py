n=int(input())
flag=0
l=list(map(int,input().split()))
for i in l:
    if l.count(i)==1:
       break
if flag==0:
    print("duplicate")
else:
    print("unique")
