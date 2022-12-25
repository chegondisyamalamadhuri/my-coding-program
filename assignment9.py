n=int(input())
n1=0
n2=1
sum=0
i=0
while(i<n):
    print(n1,end=" ")
    sum=sum+n1
    n3=n1+n2
    n1=n2
    n2=n3
    i=i+1
print("\nThe Sum of Fibonacci Series Numbers = %d" %sum)
