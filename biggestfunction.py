#way 1
def myfunction(n1,n2):
  if n1>n2:
      print('n1 is big')
  else:
      print('n2 is big')
      
num1=int(input())
num2=int(input())
myfunction(num1,num2)



 # WAY-2
  def myfunction(n1,n2):
  if n1>n2:
      return "n1 is big"
  else:
      return "n2 is big" 
      
n1=int(input())
n2=int(input())
print(myfunction(n1,n2))


# WAY-3
def myfunction(n1,n2):
  if n1>n2:
      return "n1 is big"
  else:
      return "n2 is big" 
      
n1=int(input())
n2=int(input())
if(myfunction(n1,n2)):
    print("n1 is big")
else:
    print("n2 is big")
