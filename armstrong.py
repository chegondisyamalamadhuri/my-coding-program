n= int(input())
i= 0
temp = n
while temp > 0:
    digit = temp % 10
    i += digit * digit * digit
    temp = temp//10
if i==n:
    print('It is an Armstrong number')
else:
    print('It is not an Armstrong number')
 
