s=input()
l=[]
for i in s:
    l.append(ord(i))

for i in range(0,len(l)-1):
    if l[i]+1!=l[i+1]:
        print(l[i]+1)
        break
