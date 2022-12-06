n=int(input("Enter number: "))
i=0
while(n>0):
    dig=n%10
    i=i*10+dig
    n=n//10
print("Reverse of the number:",i)
