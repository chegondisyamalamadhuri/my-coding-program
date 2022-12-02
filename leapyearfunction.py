# WAY-1
def myfunction(n):
 if n%4==0 and n%100!=0:
    print('yes')
 elif n%400==0:
    print('yes')
 else:
    print('no')
    
n=int(input())
myfunction(n)


# WAY-2
def myfunction(n):
 if n%4==0 and n%100!=0:
    return 'yes'
 elif n%400==0:
    return 'yes'
 else:
    return 'no'
    
n=int(input())
print(myfunction(n))


# WAY-3
def myfunction(n):
 if n%4==0 and n%100!=0:
    return 'yes'
 elif n%400==0:
    return 'yes'
 else:
    return 'no'
    
n=int(input())
if(myfunction(n)):
    print('yes')
else:
    print('no')
