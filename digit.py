str=input()
n=len(str)
c=0
for i in range(0,n):
   if str[i].isdigit()==1:
       c=c+1
print(c)
