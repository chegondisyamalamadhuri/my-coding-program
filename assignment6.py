def ishappy(n):
    sum=0
    while(n!=0):
        r=n%10
        sum=sum+(r*r)
        n=n//10
    return sum
n=int(input())
for i in range(1,n+1):
    n=ishappy(n)
if n==1 or n==7:
    print("Happy number")
else:
    print("Not a happy number")

