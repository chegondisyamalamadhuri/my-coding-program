# WAY-1
def myfunction(age):
    if age>=18:
        print('yes')
    else:
        print('no')
         
age=int(input())
myfunction(age)



# WAY_2
def myfunction(age):
    if age>=18:
        return 'yes'
    else:
        return 'no'
         
age=int(input())
print(myfunction(age))


# WAY-3
def myfunction(age):
    if age>=18:
        return 'yes'
    else:
        return 'no'
         
age=int(input())
if myfunction(age):
    print('yes')
else:
    print('no')
