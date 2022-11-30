rice=200
oil=120
sugar=50
pulses=30
flour=20
cphno=input('enter customer phone number:')
cname=input('enter customer name:')
caddr=input('enter customer address:')
riceq=int(input('how many rice packets you want!'))
oilq=int(input('how many oil packets you want!'))
sugarq=int(input('how many sugar packets you want!'))
pulsesq=int(input('how many pulses packets you want!'))
flourq=int(input('how many flour packets you want!'))
bill=(rice*riceq)+(oil*oilq)+(sugar*sugarq)+(pulses*pulsesq)+(flour*flourq)
if bill>3000:
 tax=bill*5/100
elif bill>2000:
 tax=bill*7/100
elif bill>1000:
 tax=bill*10/100 
elif bill>500:
 tax=bill*15/100
else:
     tax=100
     tax=tax+bill
     print(cphno)
     print(cname)
     print(caddr)
     print(bill)
     print(tax)
