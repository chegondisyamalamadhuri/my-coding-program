def ishappy(n):
    sum=0
    while(n>0):
     
        rem=n%10
        sum=sum+rem*rem
        n=n//10
    return sum
n=int(input())
while(n>9):
    n=ishappy👎
if n==1 or n==7:
    print("happy number")
else:
    print("not happy number")
print("n value=",n-1)
